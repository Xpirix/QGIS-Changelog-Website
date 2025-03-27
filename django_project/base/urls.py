# coding=utf-8
"""Urls for changelog application."""
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings

from .views import (
    custom_404,
    UserDetailView,
    UserUpdateView,
)
from .api_views.stripe_intent import StripeIntent

urlpatterns = [
    # basic app views
    # url(r'^$',
    #     view=ProjectListView.as_view(),
    #     name='home'),

    url(r'^profile/$',
        view=UserDetailView.as_view(),
        name='user-profile'),
    url(r'^edit-profile/(?P<pk>[\w-]+)/$',
        view=UserUpdateView.as_view(),
        name='edit-profile'),
    url(r'^stripe-intent/(?P<amount>[\d-]+)/$',
        view=StripeIntent.as_view(),
        name='stripe-intent'),
]

# Prevent cloudflare from showing an ad laden 404 with no context
handler404 = custom_404

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT})]
