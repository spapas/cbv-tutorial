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
#       url(r'^v5/$', views.DefaultCustomClassView.as_view(), name='v5'),
    url(r'^v6/$', views.HeaderPrefixNo1CustomClassView.as_view(), name='v6'),
    url(r'^v7/$', views.HeaderPrefixNo2CustomClassView.as_view(), name='v7'),
    url(r'^v8/$', views.HeaderPrefixNo12CustomClassView.as_view(), name='v8'),
    url(r'^v9/$', views.HeaderPrefixNo21CustomClassView.as_view(), name='v9'),
    url(r'^v10/$', views.ContextMixin12CustomClassView.as_view(), name='v10'),
    url(r'^v11/$', views.HeaderPrefixNo1ContextMixin2CustomClassView.as_view(), name='v11'),
]
