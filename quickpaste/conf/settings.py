# coding: utf-8
from django.conf import settings

__all__ = ('TINYMCE_URL', 'BUTTON_IMG_URL', 'IMG_SIZE', 'IMG_SIZE_THUMB', 'UPLOAD_DIR_NAME')

LANGUAGES = ('en', 'de', 'ru')
DEFAULT_IMG_SIZE = (1024, 768)
DEFAULT_IMG_SIZE_THUMB = (600, 600)
DEFAULT_BUTTON_IMG = 'button_en.gif'
DEFAULT_UPLOAD_DIR_NAME = 'uploads/users'

TINYMCE_URL = getattr(settings, 'QUICKPASTE_TINYMCE_URL', settings.STATIC_URL + 'tiny_mce/')

# Select button
BUTTON_IMG_URL = getattr(settings, 'QUICKPASTE_BUTTON_IMG_URL', None)
if BUTTON_IMG_URL is None:
    lang = settings.LANGUAGE_CODE.split('-')[0]
    lang = lang.lower()
    lang = lang if lang in LANGUAGES else 'en'
    button_img = 'button_%s.gif' % lang
    BUTTON_IMG_URL = TINYMCE_URL + ('plugins/quickpaste/img/%s' % button_img)

IMG_SIZE = getattr(settings, 'QUICKPASTE_IMG_SIZE', DEFAULT_IMG_SIZE)
IMG_SIZE_THUMB = getattr(settings, 'QUICKPASTE_IMG_SIZE_THUMB', DEFAULT_IMG_SIZE_THUMB)
UPLOAD_DIR_NAME = getattr(settings, 'QUICKPASTE_UPLOAD_DIR_NAME', DEFAULT_UPLOAD_DIR_NAME)