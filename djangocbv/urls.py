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
    path('articles/detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('articles/remove/<int:pk>/', views.ArticleRemoveView.as_view(), name='article-remove'),
    path('articles/unpublish/<int:pk>/', views.ArticleUnpublishView.as_view(), name='article-unpublish'),
    
    path('documents/', views.DocumentListView.as_view(), name='document-list'),
    path('documents/create/', views.DocumentCreateView.as_view(), name='document-create'),
    path('documents/update/<int:pk>/', views.DocumentUpdateView.as_view(), name='document-update'),
    path('documents/detail/<int:pk>/', views.DocumentDetailView.as_view(), name='document-detail'),
    path('documents/remove/<int:pk>/', views.DocumentRemoveView.as_view(), name='document-remove'),
    path('documents/unpublish/<int:pk>/', views.DocumentUnpublishView.as_view(), name='document-unpublish'),

    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
]
