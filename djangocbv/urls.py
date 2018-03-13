from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.DjangoHomeCustomClassView.as_view(), name='home_django'),
    path('django_better_ccv/', views.DjangoBetterCustomClassView.as_view(), name='django_better_ccv'),
    path('django_header_context_better_ccv/', views.DefaultHeaderContextDjangoBetterCustomClassView.as_view(), name='django_header_context_better_ccv'),

    path('articles/', views.ArticleListView.as_view(), name='article-list'),
    path('articles/create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('articles/update/<int:pk>/', views.ArticleUpdateView.as_view(), name='article-update'),

    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
]
