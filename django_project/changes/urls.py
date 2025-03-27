# coding=utf-8
# flake8: noqa
"""Urls for changelog application."""

from django.urls import re_path as url, include  # noqa
from django.views.static import serve

from django.conf import settings

from .feeds.version import RssVersionFeed, AtomVersionFeed
from .feeds.entry import RssEntryFeed, AtomEntryFeed
from changes.api_views.lock_version import LockVersion, UnlockVersion
from .views import (
    redirect_root,
    # Category
    CategoryDetailView,
    CategoryDeleteView,
    CategoryCreateView,
    CategoryListView,
    CategoryOrderView,
    CategoryOrderSubmitView,
    JSONCategoryListView,
    CategoryUpdateView,

    # Version
    VersionMarkdownView,
    VersionDetailView,
    VersionThumbnailView,
    VersionDeleteView,
    VersionCreateView,
    VersionListView,
    VersionUpdateView,
    VersionDownload,
    VersionDownloadMd,
    VersionDownloadGnu,
    VersionSponsorDownload,

    # Entry
    EntryDetailView,
    EntryDeleteView,
    EntryCreateView,
    EntryUpdateView,
    EntryOrderView,
    EntryOrderSubmitView,

    FetchGithubPRs,
    FetchRepoLabels,
    FetchCategory,
    download_all_referenced_images,
)

urlpatterns = [
    # Root
    url(r'^$', redirect_root, name='homepage'),
    # Category management

    # This view is only accessible via ajax
    url(r'^json-category/list/(?P<version>\d+)/$',
        view=JSONCategoryListView.as_view(),
        name='json-category-list'),
    url(r'^category/list/$',
        view=CategoryListView.as_view(),
        name='category-list'),
    url(r'^category/order/$',
        view=CategoryOrderView.as_view(),
        name='category-order'),
    url(r'^category/submit_order/$',
        view=CategoryOrderSubmitView.as_view(),
        name='category-submit-order'),
    url(r'^category/(?P<slug>[\w-]+)/$',
        view=CategoryDetailView.as_view(),
        name='category-detail'),
    url(r'^category/(?P<slug>[\w-]+)/delete/$',
        view=CategoryDeleteView.as_view(),
        name='category-delete'),
    url(r'^create-category/$',
        view=CategoryCreateView.as_view(),
        name='category-create'),
    url(r'^category/(?P<slug>[\w-]+)/update/$',
        view=CategoryUpdateView.as_view(),
        name='category-update'),

    # Version management
    url(r'^version/fetch-github-pr/$',
        view=FetchGithubPRs.as_view(),
        name='fetch-pr-github'),
    url(r'^version/fetch-github-label/$',
        view=FetchRepoLabels.as_view(),
        name='fetch-labels-github'),
    url(r'^version/fetch-category/$',
        view=FetchCategory.as_view(),
        name='fetch-category'),
    url(r'^version/list/$',
        view=VersionListView.as_view(),
        name='version-list'),
    url(r'^version/(?P<slug>[\w.-]+)/download-referenced-images/$',
        view=download_all_referenced_images,
        name='download-referenced-images'),
    url(r'^version/(?P<slug>[\w.-]+)/markdown/$',
        view=VersionMarkdownView.as_view(),
        name='version-markdown'),
    url(r'^version/(?P<slug>[\w.-]+)/$',
        view=VersionDetailView.as_view(),
        name='version-detail'),
    url(r'^version/(?P<slug>[\w.-]+)/thumbs/$',
        view=VersionThumbnailView.as_view(),
        name='version-thumbs'),
    url(r'^version/(?P<slug>[\w.-]+)/delete/$',
        view=VersionDeleteView.as_view(),
        name='version-delete'),
    url(r'^create-version/$',
        view=VersionCreateView.as_view(),
        name='version-create'),
    url(r'^version/(?P<slug>[\w.-]+)/update/$',
        view=VersionUpdateView.as_view(),
        name='version-update'),
    url(r'^version/(?P<slug>[\w.-]+)/download/$',
        view=VersionDownload.as_view(),
        name='version-download'),
    url(r'^version/(?P<slug>[\w.-]+)/md/$',
        view=VersionDownloadMd.as_view(),
        name='version-download-md'),
    url(r'^version/(?P<slug>[\w.-]+)/gnu/$',
        view=VersionDownloadGnu.as_view(),
        name='version-download-gnu'),
    url(r'^version/(?P<slug>[\w.-]+)/downloadmember/$',
        view=VersionSponsorDownload.as_view(),
        name='version-sponsor-download'),
    url(r'^version/(?P<slug>[\w.-]+)/locked/$',
        view=LockVersion.as_view(),
        name='version-locked'),
    url(r'^version/(?P<slug>[\w.-]+)/unlocked/$',
        view=UnlockVersion.as_view(),
        name='version-unlocked'),

    # Changelog entry management
    url(r'^entry/(?P<pk>\d+)$',
        view=EntryDetailView.as_view(),
        name='entry-detail'),
    url(r'^entry/delete/(?P<pk>\d+)$',
        view=EntryDeleteView.as_view(),
        name='entry-delete'),
    url(r'^(?P<version_slug>[\w.-]+)/create-entry/$',
        view=EntryCreateView.as_view(),
        name='entry-create'),
    url(r'^entry/update/(?P<pk>\d+)$',
        view=EntryUpdateView.as_view(),
        name='entry-update'),
    url(r'^version/(?P<version_pk>[\w.-]+)/order/(?P<category_pk>[\w-]+)$',
        view=EntryOrderView.as_view(),
        name='entry-order'),
    url(r'^version/(?P<version_pk>[\w.-]+)/submit-order/(?P<category_pk>[\w-]+)$',
        view=EntryOrderSubmitView.as_view(),
        name='entry-submit-order'),

    # Feeds
    url(r'^rss/latest-version/$',
        view=RssVersionFeed(),
        name='latest-version-rss-feed'),
    url(r'^atom/latest-version/$',
        view=AtomVersionFeed(),
        name='latest-version-atom-feed'),
    url(r'^rss/latest-entry/$',
        view=RssEntryFeed(),
        name='latest-entry-rss-feed'),
    url(r'^atom/latest-entry/$',
        view=AtomEntryFeed(),
        name='latest-entry-atom-feed'),

    # Feeds specific version and projects
    url(r'^version/(?P<version_slug>[\w.-]+)/rss$',
        view=RssEntryFeed(),
        name='entry-rss-feed'),
    url(r'^version/(?P<version_slug>[\w.-]+)/atom$',
        view=AtomEntryFeed(),
        name='entry-atom-feed'),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT})]
