# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.views.generic.base import View

from core.views import HomeCustomClassView

from core.mixins import DefaultHeaderMixin, DefaultContextMixin, UrlPatternsMixin

from .models import Article, Category, Document
from .forms import ArticleForm, DocumentForm
from .filters import ArticleFilter, DocumentFilter
from .mixins import *


class DjangoHomeCustomClassView(UrlPatternsMixin, TemplateView, ):
    template_name = 'django_cbv_home.html'

    def get_urlpatterns(self):
        from djangocbv.urls import urlpatterns

        return [ p for p in urlpatterns if ':' not in p.pattern.describe()]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urls'] = self.render_patterns()
        return context


class DjangoBetterCustomClassView(View, ):
    header = ''
    context =''

    def get_header(self, ):
        return self.header if self.header else ""

    def get_context(self , ):
        return self.context if self.context else []

    def render_context(self):
        context = self.get_context()
        if context:
            return '<br />'.join(context)
        return ""

    def get(self, *args, **kwargs):
        resp = """
            <html>
                <head>
                    <link rel="stylesheet" href="https://unpkg.com/normalize.css@7.0.0/normalize.css" type="text/css"/>
                    <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css"/>
                </head>
                <body>
                    <h1>{header}</h1>
                    {body}
                </body>
            </html>
        """.format(
                header=self.get_header(), body=self.render_context(),
            )
        return HttpResponse(resp)


class DefaultHeaderContextDjangoBetterCustomClassView(DefaultHeaderMixin, DefaultContextMixin, DjangoBetterCustomClassView):
    pass


class ArticleListView(ContentListMixin, ListView):
    model = Article
    context_object_name = 'articles'
    filter_class = ArticleFilter
    

class ArticleCreateView(ContentCreateMixin, RedirectToArticlesMixin, CreateView):
    model = Article
    form_class = ArticleForm


class ArticleUpdateView(ContentUpdateMixin, RedirectToArticlesMixin, UpdateView):
    model = Article
    form_class = ArticleForm

class ArticleDetailView(HideRemovedMixin, DetailView):
    model = Article
    context_object_name = 'article'

    def get_template_names(self):
        if self.request.is_ajax() or self.request.GET.get('partial'):
            return 'djangocbv/_article_content_partial.html'
        return super().get_template_names()


class ArticleRemoveView(ContentRemoveMixin, RedirectToArticlesMixin, UpdateView):
    model = Article


class ArticleUnpublishView(ContentUnpublishMixin, RedirectToArticlesMixin, UpdateView):
    model = Article


class CategoryListView(ExportCsvMixin, AdminOrPublisherPermissionRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.annotate(article_cnt=Count('article'), document_cnt=Count('document'))


class CategoryCreateView(CreateSuccessMessageMixin, RedirectToHomeMixin, AdminOrPublisherPermissionRequiredMixin, CreateView):
    model = Category
    fields = ['name']


class CategoryUpdateView(UpdateSuccessMessageMixin, RedirectToHomeMixin, AdminOrPublisherPermissionRequiredMixin, UpdateView):
    model = Category
    fields = ['name']


class DocumentListView(ContentListMixin, ListView):
    model = Document
    context_object_name = 'documents'
    filter_class = DocumentFilter


class DocumentCreateView(ContentCreateMixin, RedirectToDocumentsMixin, CreateView):
    model = Document
    form_class = DocumentForm


class DocumentUpdateView(ContentUpdateMixin, RedirectToDocumentsMixin, UpdateView):
    model = Document
    form_class = DocumentForm


class DocumentDetailView(HideRemovedMixin, DetailView):
    model = Document
    context_object_name = 'document'


class DocumentRemoveView(ContentRemoveMixin, RedirectToDocumentsMixin, UpdateView):
    model = Document


class DocumentUnpublishView(ContentUnpublishMixin, RedirectToDocumentsMixin, UpdateView):
    model = Document

    
class DynamicTemplateView(TemplateView):
    def get_template_names(self):
        what = self.kwargs['what']
        return '{0}.html'.format(what)
        