from django.forms import ModelForm
from .models import Article, Document, Category


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'owned_by', 'title', 'content', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        
        if not self.request.user.has_perm('djangocbv.admin_access'):
            self.fields.pop('owned_by')