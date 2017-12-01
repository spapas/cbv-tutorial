# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json

from . import mixins

class CustomClassView:
    context = []
    header = ''

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        for (k,v) in kwargs.items():
            setattr(self, k, v)

    def render(self):
        print ("Custom Class View render")
        return """
            <html>
                <body>
                    <h1>{header}</h1>
                    {body}
                </body>
            </html>
        """.format(
                header=self.header, body='<br />'.join(self.context),
            )

    @classmethod
    def as_view(cls, *args, **kwargs):
        def view(request, ):
            instance = cls(**kwargs)
            return HttpResponse(instance.render())

        return view

class InheritsCustomClassView(CustomClassView, ):
    header = "Hi"
    context = ['test', 'test2' ]


class BetterCustomClassView(CustomClassView, ):
    def get_header(self, ):
        print ("Better Custom Class View get_header")
        return self.header if self.header else ""

    def get_context(self , ):
        return self.context if self.context else []

    def render_context(self):
        context = self.get_context()
        if context:
            return '<br />'.join(context)
        return ""

    def render(self):
        print ("Better Custom Class View render")
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


class DefaultHeaderBetterCustomClassView(BetterCustomClassView, ):
    def get_header(self, ):
        return self.header if self.header else "DEFAULT HEADER"

class DefaultContextBetterCustomClassView(BetterCustomClassView, ):
    def get_context(self, ):
        return self.context if self.context else ["DEFAULT CONTEXT"]

class JsonCustomClassView:
    header = ''
    context = []

    def get_header(self, ):
        return self.header if self.header else ""

    def get_context(self, ):
        return self.context if self.context else []

    @classmethod
    def as_view(cls, *args, **kwargs):
        def view(request, ):
            instance = cls(**kwargs)
            return HttpResponse(json.dumps({
                'header': instance.get_header(),
                'context': instance.get_context(),
            }))

        return view


class DefaultHeaderJsonCustomClassView(DefaultHeaderBetterCustomClassView, JsonCustomClassView):
    pass
print (DefaultHeaderJsonCustomClassView.__mro__)
class JsonDefaultHeaderCustomClassView(JsonCustomClassView, DefaultHeaderBetterCustomClassView):
    pass
print (JsonDefaultHeaderCustomClassView.__mro__)
class DefaultHeaderContextCustomClassView(DefaultHeaderBetterCustomClassView, DefaultContextBetterCustomClassView):
    pass
print (DefaultHeaderContextCustomClassView.__mro__)

class DefaultHeaderMixinBetterCustomClassView(mixins.DefaultHeaderMixin, BetterCustomClassView):
    pass

class DefaultContextMixinBetterCustomClassView(mixins.DefaultContextMixin, BetterCustomClassView):
    pass

class DefaultHeaderContextMixinBetterCustomClassView(mixins.DefaultHeaderMixin, mixins.DefaultContextMixin, BetterCustomClassView):
    pass


class JsonDefaultHeaderMixinCustomClassView(mixins.DefaultHeaderMixin, JsonCustomClassView):
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

class HomeCustomClassView(BetterCustomClassView, ):
    def render_context(self):
        from core.urls import urlpatterns
        from django.urls import reverse
        ctx = "<br />".join(
            ['<a href="{0}">{1}</a>'.format(reverse(p.name), p.name) for p in urlpatterns]
        )
        return ctx

