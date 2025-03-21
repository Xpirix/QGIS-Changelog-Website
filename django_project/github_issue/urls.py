# coding=utf-8
"""Urls for submitting github support requests."""
from django.urls import re_path as url
from django.conf import settings
from django.views.static import serve

from .views import GithubIssue

urlpatterns = [
    # basic app views
    url(r'^github-issue$',
        view=GithubIssue.as_view(),
        name='github-issue'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT})]
