class DefaultMixin:
    def get_header(self, ):
        print ("Default Mixin")
        return self.header if self.header else "DEFAULT HEADER"


class HeaderPrefixNo1:
    def get_header(self, ):
        if self.header:
            return "PREFIX 1: " + self.header
        return "PREFIX 1"


class HeaderPrefixNo2:
    def get_header(self, ):
        return "PREFIX 2: " + super().get_header()


class ContextMixin1:
    def get_context(self, ):
        ctx = super().get_context()
        ctx.append('data1')
        return ctx

class ContextMixin2:
    def get_context(self, ):
        ctx = super().get_context()
        ctx.append('data2')
        return ctx
