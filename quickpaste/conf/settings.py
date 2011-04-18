#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings

TINYMCE_URL = getattr(settings, 'QUICKPASTE_TINYMCE_URL', settings.MEDIA_URL+'common/tiny_mce/')
IMAGE_SIZE = getattr(settings, 'QUICKPASTE_IMAGE_SIZE', (1024, 768))
IMAGE_SIZE_THUMBNAIL = getattr(settings, 'QUICKPASTE_IMAGE_SIZE_THUMBNAIL', (600, 600))
DIRECTORY = getattr(settings, 'QUICKPASTE_DIRECTORY', 'uploads/users/')
