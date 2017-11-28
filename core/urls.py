from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.HomeCustomClassView.as_view(), name='home'),
    url(r'^v1/$', views.CustomClassView.as_view(), name='v1'),
    url(r'^v2/$', views.CustomClassView.as_view(header='Hello', context={'a': 1}, footer='Bye', ), name='v2'),
    url(r'^v3/$', views.CustomClassViewDefault.as_view(), name='v3'),
    url(r'^v4/$', views.BetterCustomClassView.as_view(), name='v4'),
    url(r'^v5/$', views.DefaultCustomClassView.as_view(), name='v5'),
    url(r'^v6/$', views.HeaderPrefixNo1CustomClassView.as_view(), name='v6'),
    url(r'^v7/$', views.HeaderPrefixNo2CustomClassView.as_view(), name='v7'),
    url(r'^v8/$', views.HeaderPrefixNo12CustomClassView.as_view(), name='v8'),
    url(r'^v9/$', views.HeaderPrefixNo21CustomClassView.as_view(), name='v9'),
    url(r'^v10/$', views.ContextMixin12CustomClassView.as_view(), name='v10'),
    url(r'^v11/$', views.HeaderPrefixNo1ContextMixin2CustomClassView.as_view(), name='v11'),
]
