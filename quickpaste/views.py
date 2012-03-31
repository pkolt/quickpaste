# coding: utf-8
import os
import re
import string
import Image
import datetime
import urlparse
from django import forms
from django.conf import settings
from django.http import Http404, parse_cookie
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from quickpaste.conf.settings import *
from quickpaste.decorators import flash_login_required

PATTERN_SPACES = re.compile(r'\s+')
PATTERN_PUNCTUATION = re.compile('[' + string.punctuation + ']+')

class UploadForm(forms.Form):
    upload = forms.FileField(label='')

class UploadView(FormView):
    form_class = UploadForm
    template_name = 'quickpaste/form.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        decorator = flash_login_required if request.method == 'POST' else login_required
        dispatch = decorator(super(UploadView, self).dispatch)
        return dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        cookie_dict = parse_cookie(self.request.META.get('HTTP_COOKIE', ''))
        session_key = cookie_dict.get(settings.SESSION_COOKIE_NAME, None)
        context.update({
            'url_timymce': TINYMCE_URL,
            'url_button': BUTTON_IMG_URL,
            'session_key': session_key
        })
        return context

    def get_today_dirname(self):
        return datetime.date.today().strftime("%Y/%m/%d")

    def translate_filename(self, filename):
        name, ext = os.path.splitext(filename)
        name = name.strip()
        name = re.sub(PATTERN_PUNCTUATION, '', name)
        name = re.sub(PATTERN_SPACES, '-', name)
        name = name.encode('trans')
        ext = ext.lower()
        return name + ext

    def generic_filename(self, path, filename):
        count = 1
        fn = filename
        while os.path.exists(os.path.join(path, fn)):
            name, ext = os.path.splitext(filename)
            fn = '%s-%d%s' % (name, count, ext)
            count += 1
        return fn

    def get_thumb_filename(self, filename):
        name, ext = os.path.splitext(filename)
        return '%s-thumb%s' % (name, ext)

    def get_title(self, filename):
        name, ext = os.path.splitext(filename)
        return name

    def upload_file(self, f, user_pk):
        context = {
            'title': self.get_title(f.name)
        }
        upload_dirs = os.path.join(UPLOAD_DIR_NAME, str(user_pk), self.get_today_dirname())
        path = os.path.join(settings.MEDIA_ROOT, upload_dirs)

        filename = self.translate_filename(f.name)
        if os.path.exists(path):
            filename = self.generic_filename(path, filename)
        else:
            os.makedirs(path)
        save_path = os.path.join(path, filename)

        f.seek(0,0)
        try:
            img = Image.open(f)
        except (IOError, OverflowError):
            # Other file
            is_img = False
            f.seek(0,0)
            open(save_path, 'wb').write(f.read())
        else:
            # Image file
            is_img = True
            if IMG_SIZE:
                img.thumbnail(IMG_SIZE, Image.ANTIALIAS)
            img.save(open(save_path, 'wb'))
            # Create thumbnail
            thumb_filename = self.get_thumb_filename(filename)
            thumb_save_path = os.path.join(path, thumb_filename)
            # width img > width thumbnail
            if img.size[0] > IMG_SIZE_THUMB[0]:
                img.thumbnail(IMG_SIZE_THUMB, Image.ANTIALIAS)
                img.save(open(thumb_save_path, 'wb'))
                # Url thumbnail
                context['thumb_url'] = urlparse.urljoin(settings.MEDIA_URL, os.path.join(upload_dirs, thumb_filename))
        # Url file upload
        url = urlparse.urljoin(settings.MEDIA_URL, os.path.join(upload_dirs, filename))
        context.update({
            'is_img': is_img,
            'url': url,
        })
        return context

    def form_valid(self, form):
        context = self.upload_file(form.cleaned_data['upload'], self.request.user.pk)
        return render_to_response('quickpaste/content.html', context)

    def form_invalid(self, form):
        raise Http404