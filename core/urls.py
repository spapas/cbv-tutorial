from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.HomeCustomClassView.as_view(), name='home'),
    url(r'^ccv-empty/$', views.CustomClassView.as_view(), name='ccv-empty'),
    url(r'^ccv-with-values/$', views.CustomClassView.as_view(header='Hello', context=['hello', 'world', ], footer='Bye', ), name='ccv-with-values'),
    url(r'^ccv-inherits/$', views.InheritsCustomClassView.as_view(), name='ccv-inherits'),
    url(r'^default-header-bccv/$', views.DefaultHeaderBetterCustomClassView.as_view(), name='default-header-bccv'),
    url(r'^json-ccv/$', views.JsonCustomClassView.as_view(), name='json-ccv'),
    url(r'^default-header-json-ccv/$', views.DefaultHeaderJsonCustomClassView.as_view(), name='default-header-json-ccv'),
    url(r'^json-default-header-ccv/$', views.JsonDefaultHeaderCustomClassView.as_view(), name='json-default-header-ccv'),
    url(r'^default-header-context-ccv/$', views.DefaultHeaderContextCustomClassView.as_view(), name='default-header-context-ccv'),
    url(r'^default-header-mixin-bccv/$', views.DefaultHeaderMixinBetterCustomClassView.as_view(), name='default-header-mixin-bccv'),
    url(r'^default-context-mixin-bccv/$', views.DefaultContextMixinBetterCustomClassView.as_view(), name='default-context-mixin-bccv'),
    url(r'^default-header-context-mixin-bccv/$', views.DefaultHeaderContextMixinBetterCustomClassView.as_view(), name='default-header-context-mixin-bccv'),
    url(r'^default-header-mixin-json-ccv/$', views.JsonDefaultHeaderMixinCustomClassView.as_view(), name='default-header-mixin-json-ccv'),
    url(r'^header-prefix-bccv/$', views.HeaderPrefixBetterCustomClassView.as_view(), name='header-prefix-bccv'),
    url(r'^header-prefix-default-bccv/$', views.HeaderPrefixDefaultBetterCustomClassView.as_view(), name='header-prefix-default-bccv'),
    url(r'extra-context-12-bccv/$', views.ExtraContext12BetterCustomClassView.as_view(), name='extra-context-12-bccv'),
    url(r'extra-context-21-bccv/$', views.ExtraContext21BetterCustomClassView.as_view(), name='extra-context-21-bccv'),
    url(r'all-together-now-bccv/$', views.AllTogetherNowBetterCustomClassView.as_view(), name='all-together-now-bccv'),
]
