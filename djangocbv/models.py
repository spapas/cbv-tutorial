from django.conf import settings
from django.db import models


STATUS_CHOICES = (
    ('DRAFT', 'Draft', ),
    ('PUBLISHED', 'Published', ),
    ('REMOVED', 'Removed', ),
)


class Category(models.Model):
    name = models.CharField(max_length=128, )


class AbstractGeneralInfo(models.Model):
    category = models.ForeignKey('category', on_delete=models.PROTECT, )
    created_on = models.DateTimeField(auto_now_add=True, )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='%(class)s_created_by', )
    modified_on = models.DateTimeField(auto_now=True, )
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='%(class)s_modified_by', )
    published_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Article(AbstractGeneralInfo):
    title = models.CharField(max_length=128, )
    content = models.TextField()



class Document(AbstractGeneralInfo):
    description = models.CharField(max_length=128, )
    file = models.FileField()
