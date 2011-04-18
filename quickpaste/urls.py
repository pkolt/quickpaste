#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from quickpaste.views import FormView

urlpatterns = patterns('',
    url(r'^upload/$', 'quickpaste.views.upload_view', name='quickpaste_upload'),
    url(r'^form/$', FormView.as_view(), name='quickpaste_form'),
)