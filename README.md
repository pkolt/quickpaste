# QuickPaste. Плагин к TinyMCE для загрузки файлов.

# Возможности
- быстрая загрузка файлов, лёгок в понимании
- автоматический ресайзинг изображений
- автоматическая транстилерация имен файлов
- вставка ссылки в редактор по окончания процесса загрузки


# Зависимости
- Django 1.3
- trans (http://pypi.python.org/pypi/trans/1.2)
- PIL
- django-tinymce (рекомендуем, http://code.google.com/p/django-tinymce/)

# Установка
1. Добавить в `quickpaste` INSTALLED_APPS (settings.py)
2. Добавить `(r'^quickpaste/', include('quickpaste.urls')),` в patterns (urls.py)
3. Добавить плагин в настройках TinyMCE

# Настройка
Настройка конфигурации приложения в файле settings.py

URL каталога WYSIWYG-редактора TinyMCE (http://tinymce.moxiecode.com/)
TINYMCE_URL = settings.MEDIA_URL+'common/tiny_mce/'

Размеры файла изображения
IMAGE_SIZE = (1024, 768) #
IMAGE_SIZE = () # будут сохранены исходные размеры

IMAGE_SIZE_THUMBNAIL = (600, 600) # размеры миниатюры

DIRECTORY = 'uploads/users/' # директория для загрузки файлов

# Благодарности

В проекте был использован Flash-загрузчик Uploadify.
http://www.uploadify.com/documentation/
