# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import HttpResponse

from core.views import HomeCustomClassView
from core.mixins import DefaultHeaderMixin, DefaultContextMixin


class DjangoHomeCustomClassView(HomeCustomClassView, ):
    def get_urlpatterns(self):
        from djangocbv.urls import urlpatterns
        return urlpatterns


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


class DefaultHeaderContextDjangoBetterCustomClassView( DefaultHeaderMixin, DefaultContextMixin, DjangoBetterCustomClassView):
    pass

