import django_filters
from .models import Article, Document

class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = {
            'title': ['icontains']
        }
        
        
class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields = {
            'description': ['icontains']
        }