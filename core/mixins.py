from django.urls import reverse

class DefaultHeaderMixin:
    def get_header(self, ):
        return self.header if self.header else "DEFAULT HEADER"


class DefaultContextMixin:
    def get_context(self, ):
        return self.context if self.context else ["DEFAULT CONTEXT"]


class HeaderPrefixMixin:
    def get_header(self, ):
        return "PREFIX: " + super().get_header()


class DefaultHeaderSuperMixin:
    def get_header(self, ):
        return super().get_header() if super().get_header() else "DEFAULT HEADER"


class ExtraContext1Mixin:
    def get_context(self, ):
        ctx = super().get_context()
        ctx.append('data1')
        return ctx


class ExtraContext2Mixin:
    def get_context(self, ):
        ctx = super().get_context()
        ctx.insert(0, 'data2')
        return ctx


class UrlPatternsMixin:
    def render_patterns(self):
        ctx = "<br />".join(
            ['<a href="{0}">{1}</a>'.format(reverse(p.name), p.name) for p in self.get_urlpatterns()]
        )
        return ctx        