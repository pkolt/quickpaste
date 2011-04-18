#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import trans
import urlparse
import string
import datetime
import Image
from django import forms
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import Http404, parse_cookie
from django.utils.decorators import method_decorator
from quickpaste.conf.settings import *
from quickpaste.decorators import flash_login_required


class UploadForm(forms.Form):
    """ Форма загрузки """
    upload = forms.FileField(label='')

class FormView(TemplateView):
    """ Страница отображения формы для загрузки файла """
    template_name = 'quickpaste/base.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FormView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        cookie_dict = parse_cookie(self.request.META.get('HTTP_COOKIE', ''))
        session_key = cookie_dict.get(settings.SESSION_COOKIE_NAME, None)
        context = {'TINYMCE_URL': TINYMCE_URL, 'session_key': session_key, 'form': UploadForm()}
        kwargs.update(context)
        return kwargs


@csrf_exempt
@flash_login_required
def upload_view(request):
    """ Обработка загрузки файла """
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            context = save_file(request.user.username, form.cleaned_data['upload'])
            return render_to_response('quickpaste/link.html', context)
    raise Http404


def save_file(username, file):
    # путь загрузки файла /[directory]/[username]/[year]/[month]/[day]/
    _path = os.path.join(DIRECTORY, username, datetime.date.today().strftime("%Y/%m/%d"))

    # создадим каталоги если их нет
    path = os.path.join(settings.MEDIA_ROOT, _path)
    if not os.path.exists(path):
        os.makedirs(path)

    # транстилерация имени файла
    title, filename = file.name, file.name.encode('trans')
    symbols = string.punctuation.replace('.',' ')
    table = string.maketrans(symbols, "-"*len(symbols))
    filename = str(filename).translate(table)

    # если файл с таким именем уже существует, подобрать другое имя
    while os.path.exists(os.path.join(path, filename)):
        filename = '_%s' % filename

    context = {'title': title, 'url': urlparse.urljoin(settings.MEDIA_URL, os.path.join(_path, filename))}

    # ресайзинг изображения
    try:
        file.seek(0,0)
        im = Image.open(file)
    except:
        is_image = False
        file.seek(0,0)
        open(os.path.join(path, filename), 'wb').write(file.read())
    else:
        is_image = True
        if IMAGE_SIZE:
            im.thumbnail(IMAGE_SIZE, Image.ANTIALIAS)
        im_path = os.path.join(path, filename)
        im.save(open(im_path, 'wb'))

        w, h = im.size
        if w > IMAGE_SIZE_THUMBNAIL[0]:
            _path = os.path.join(_path, 'thumbnail')
            path = os.path.join(settings.MEDIA_ROOT, _path)
            if not os.path.exists(path):
                os.makedirs(path)
            f_thumb = open(os.path.join(path, filename), 'wb')
            thumb = Image.open(open(im_path))
            thumb.thumbnail(IMAGE_SIZE_THUMBNAIL, Image.ANTIALIAS)
            thumb.save(f_thumb)
            f_thumb.close()
            context.update({'thumb': urlparse.urljoin(settings.MEDIA_URL, os.path.join(_path, filename))})
        
    context.update({'is_image': is_image})
    return context