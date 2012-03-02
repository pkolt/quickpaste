# coding: utf-8
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.conf import settings

def flash_login_required(function):
    """
    Decorator that authenticates the user's session key packed in POST-variable.
    The use caused by the fact that the flash-loader does not otprovlyaet Cookie in which a session key stored user.
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