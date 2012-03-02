==============================================
QuickPaste. TinyMCE plugin for uploading files
==============================================

Features
========

- fast downloading files
- auto resayzing images
- automatic transliteration of the names of files
- insert a link to the editor by the end of the boot process

Depending
=========

- PIL
- Django >= 1.3
- django-tinymce (http://code.google.com/p/django-tinymce/)
- trans (http://pypi.python.org/pypi/trans/1.3)

Installation
============

1. Add ``quickpaste`` in INSTALLED_APPS
2. Add ``(r'^quickpaste/', include('quickpaste.urls'))`` in urlpatterns
3. Connect plugin quickpaste and add ``quickpaste`` button in configuration file TinyMCE

Settings
========

settings.py ::

    # Url timy mce folder
    QUICKPASTE_TINYMCE_URL = settings.STATIC_URL + 'tiny_mce/'

    # Customize button `Select the file`
    # Size 120x30 pixels
    QUICKPASTE_BUTTON_IMG_URL = None

    # Change the size of the original image
    QUICKPASTE_IMG_SIZE = (1024, 768)

    # Resize thumbnail picture
    QUICKPASTE_IMG_SIZE_THUMB = (600, 600)

    # Download directory of files, relative MEDIA_ROOT
    QUICKPASTE_UPLOAD_DIR_NAME = 'uploads/users'

Changelog
=========

01.03.2012 - version 1.2.0, fix bug, remove application ``uploadtools``. Added support for German language.

18.04.2011 - version 1.0.0 first version.

Acknowledgments
===============

The draft was used by Flash-loader Uploadify.
http://www.uploadify.com/documentation/