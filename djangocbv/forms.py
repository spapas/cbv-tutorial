from django.forms import ModelForm
from .models import Article, Document, Category


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['status', 'category', 'owned_by', 'title', 'content', ]
