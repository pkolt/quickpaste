#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.conf import settings

def flash_login_required(function):
    """
    Декоратор, который аутентифицирует пользователя по ключу сессии упакованному в POST-переменную.
    Использование вызвано, тем что флешь-загрузчик не отпровляет Cookie в которых храниться ключ сессии пользователя.
    """
    
    def decorator(request, *args, **kwargs):
        try:
            engine = __import__(settings.SESSION_ENGINE, {}, {}, [''])
        except ImportError:
            import django.contrib.sessions.backends.db
            engine = django.contrib.sessions.backends.db
        session_data = engine.SessionStore(request.POST.get('session_key'))
        user_id = session_data['_auth_user_id']
        request.user = get_object_or_404(User, pk=user_id)
        return function(request, *args, **kwargs)
    return decorator