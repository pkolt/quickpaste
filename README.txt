==============================================
QuickPaste. TinyMCE plugin for uploading files
==============================================

Features
- fast downloading files
- auto resayzing images
- automatic transliteration of the names of files
- insert a link to the editor by the end of the boot process


Depending
- Django 1.3
- trans (http://pypi.python.org/pypi/trans/1.3)
- PIL
- django-tinymce (http://code.google.com/p/django-tinymce/)
- django-uploadtools (http://github.com/pkolt)


Installation
1. Add `quickpaste` in INSTALLED_APPS
2. Add `(r'^quickpaste/', include('quickpaste.urls'))` in urlpatterns
3. Connect plugin `quickpaste` in configuration file TinyMCE


Settings
URL каталога WYSIWYG-редактора TinyMCE (http://tinymce.moxiecode.com/)
QUICKPASTE_URL_TINYMCE = settings.STATIC_URL+'tiny_mce/' - URL to a folder tiny_mce
QUICKPASTE_URL_BUTTON - Customize button `Select the file`
QUICKPASTE_IMAGE_SIZE = (1024, 768) - Change the size of the original image
QUICKPASTE_IMAGE_SIZE_THUMBNAIL = (600, 600) - Resize thumbnail picture
QUICKPASTE_DIRECTORY = 'uploads/users' - Download directory of files, regarding MEDIA_URL

Acknowledgments
The draft was used by Flash-loader Uploadify.
http://www.uploadify.com/documentation/
