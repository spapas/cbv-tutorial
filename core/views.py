# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import mixins

class CustomClassView:
    context = []
    header = ''

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        for (k,v) in kwargs.items():
            setattr(self, k, v)

    def render(self):
        return """
            <html>
                <body>
                    <h1>{header}</h1>
                    {body}
                </body>
            </html>
        """.format(
                header=self.header, body=self.render_context(),
            )

    def render_context(self):
        return '<br />'.join(self.context)

    @classmethod
    def as_view(cls, *args, **kwargs):
        def view(request, ):
            instance = cls(**kwargs)
            return HttpResponse(instance.render())

        return view

class HomeCustomClassView(CustomClassView, ):
    def render_context(self):
        from core.urls import urlpatterns
        from django.urls import reverse
        ctx = "<br />".join(
            ['<a href="{0}">{1}</a>'.format(reverse(p.name), p.name) for p in urlpatterns]
        )
        return ctx

class CustomClassViewDefault(CustomClassView, ):
    header = "Hi"
    fotter = "Bye bye"
    context = {'test', 'test2' }


class BetterCustomClassView(CustomClassView, ):
    def get_header(self, ):
        print ("Better Custom Class View")
        return self.header if self.header else ""

    def get_context(self , ):
        return self.context if self.context else []

    def render_context(self):
        context = self.get_context()
        if context:
            return '<br />'.join(context)
        return ""

    def render(self):
        return """
            <html>
                <body>
                    <h1>{header}</h1>
                    {body}
                </body>
            </html>
        """.format(
                header=self.get_header(), body=self.render_context(),
            )

class DefaultCustomClassView(mixins.DefaultMixin, BetterCustomClassView):
    pass


class HeaderPrefixNo1CustomClassView(mixins.HeaderPrefixNo1, BetterCustomClassView):
    header = "Header 1"

class HeaderPrefixNo2CustomClassView(mixins.HeaderPrefixNo2, BetterCustomClassView):
    header = "Header 2"

class HeaderPrefixNo12CustomClassView(mixins.HeaderPrefixNo1, mixins.HeaderPrefixNo2, BetterCustomClassView):
    header = "Header 12"

class HeaderPrefixNo21CustomClassView(mixins.HeaderPrefixNo2, mixins.HeaderPrefixNo1, BetterCustomClassView):
    header = "Header 21"

class ContextMixin12CustomClassView(mixins.ContextMixin1, mixins.ContextMixin2, BetterCustomClassView):
    context = ['Class data']

class HeaderPrefixNo1ContextMixin2CustomClassView(mixins.HeaderPrefixNo1, mixins.ContextMixin2, BetterCustomClassView):
    header = "Better"
    context = ['Much better']
