#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings

# Path Django CMS
if 'cms' in settings.INSTALLED_APPS:
    from django.core.urlresolvers import reverse
    from cms.middleware.toolbar import ToolbarMiddleware
    
    def toolbar_path(funct):
        def wrapper(self, request, response):
            if request.path_info.startswith(reverse('quickpaste')):
                return False
            else:
                return funct(self, request, response)
        return wrapper

    ToolbarMiddleware.show_toolbar = toolbar_path(ToolbarMiddleware.show_toolbar)