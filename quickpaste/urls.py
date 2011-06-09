#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from quickpaste.views import UploadView

urlpatterns = patterns('',
    url(r'^$', UploadView.as_view(), name='quickpaste'),
)