from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.DjangoHomeCustomClassView.as_view(), name='home_django'),
    url(r'^django_better_ccv/$', views.DjangoBetterCustomClassView.as_view(), name='django_better_ccv'),
    url(r'^django_header_context_better_ccv/$', views.DefaultHeaderContextDjangoBetterCustomClassView.as_view(), name='django_header_context_better_ccv'),
]
