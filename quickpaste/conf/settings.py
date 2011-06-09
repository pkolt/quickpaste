#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings

URL_TINYMCE = getattr(settings, 'QUICKPASTE_URL_TINYMCE', settings.STATIC_URL+'tiny_mce/')
# Select button
if hasattr(settings, 'QUICKPASTE_URL_BUTTON'):
    URL_BUTTON = getattr(settings, 'QUICKPASTE_URL_BUTTON')
else:
    button_lang = 'ru' if settings.LANGUAGE_CODE.startswith('ru') else 'en'
    URL_BUTTON = URL_TINYMCE+('plugins/quickpaste/img/button_%s.gif' % button_lang)
IMAGE_SIZE = getattr(settings, 'QUICKPASTE_IMAGE_SIZE', (1024, 768))
IMAGE_SIZE_THUMBNAIL = getattr(settings, 'QUICKPASTE_IMAGE_SIZE_THUMBNAIL', (600, 600))
DIRECTORY = getattr(settings, 'QUICKPASTE_DIRECTORY', 'uploads/users')