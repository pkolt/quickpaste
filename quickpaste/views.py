#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import Image
import os
import urlparse
from django import forms
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import Http404, parse_cookie
from django.utils.decorators import method_decorator
from uploadtools import translate_filename
from quickpaste.conf.settings import *
from quickpaste.decorators import flash_login_required

class UploadForm(forms.Form):
    """ Download Form """
    upload = forms.FileField(label='')

class FormView(TemplateView):
    """ Page displaying the form to download the file """
    template_name = 'quickpaste/base.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FormView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        cookie_dict = parse_cookie(self.request.META.get('HTTP_COOKIE', ''))
        session_key = cookie_dict.get(settings.SESSION_COOKIE_NAME, None)
        context = {'URL_TINYMCE': URL_TINYMCE, 'url_button': URL_BUTTON, 'session_key': session_key, 'form': UploadForm()}
        kwargs.update(context)
        return kwargs

@csrf_exempt
@flash_login_required
def upload_view(request):
    """ Handling file uploads """
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            context = upload_file(request.user, form.cleaned_data['upload'])
            return render_to_response('quickpaste/link.html', context)
    raise Http404

def upload_file(user, file):
    """
    Handles and stores the file

    Template File Download /[QUICKPASTE_DIRECTORY]/[user.pk]/[year]/[month]/[day]/
    """
    def choose_filename(real_path, filename):
        """ Selects a new file name if a file with that name already exists """
        while os.path.exists(os.path.join(real_path, filename)):
            filename = '_%s' % filename
        return filename

    def create_directories(real_path):
        """ Create directories """
        if not os.path.exists(real_path):
            os.makedirs(real_path)
            
    path = os.path.join(*[DIRECTORY, str(user.pk), datetime.date.today().strftime("%Y/%m/%d")])
    # Create directories
    real_path = os.path.join(settings.MEDIA_ROOT, path)
    create_directories(real_path)
    # Transliteration of the name of the file
    filename, title = translate_filename(file.name)
    filename = choose_filename(real_path, filename)
    # Context template
    context = {'title': title, 'url': urlparse.urljoin(settings.MEDIA_URL, os.path.join(path, filename))}
    # Processing of image file
    file.seek(0,0)
    is_image = False
    try:
        im = Image.open(file)
    except (IOError, OverflowError):
        file.seek(0,0)
        # Save the file, which is not an image
        open(os.path.join(real_path, filename), 'wb').write(file.read())
    else:
        is_image = True
        # Resize images to match the settings
        if IMAGE_SIZE:
            im.thumbnail(IMAGE_SIZE, Image.ANTIALIAS)
        full_path_im = os.path.join(real_path, filename)
        im.save(open(full_path_im, 'wb'))
        # Creating thumbnail images
        w, h = im.size
        if w > IMAGE_SIZE_THUMBNAIL[0]:
            path_thumb = os.path.join(path, 'thumbnail')
            real_path_thumb = os.path.join(settings.MEDIA_ROOT, path_thumb)
            create_directories(real_path_thumb)
            thumb = Image.open(open(full_path_im))
            thumb.thumbnail(IMAGE_SIZE_THUMBNAIL, Image.ANTIALIAS)
            thumb.save(open(os.path.join(real_path_thumb, filename), 'wb'))
            context.update({'thumb': urlparse.urljoin(settings.MEDIA_URL, os.path.join(path_thumb, filename))})        
    context.update({'is_image': is_image})
    return context