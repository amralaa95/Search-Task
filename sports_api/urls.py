# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import SearchResultView

urlpatterns = [
    url(r'^$', SearchResultView.as_view(), name='search'),
]