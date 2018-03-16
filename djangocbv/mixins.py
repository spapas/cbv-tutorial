from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
import csv, json

from .models import Category


class AuditableMixin:
    def form_valid(self, form, ):
        if not form.instance.created_by_id:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super().form_valid(form)


class LimitAccessMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.has_perm('djangocbv.admin_access') or self.request.user.has_perm('djangocbv.publisher_access') :
            return qs
        return qs.filter(owned_by=self.request.user)


class HideRemovedMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.has_perm('djangocbv.admin_access') or self.request.user.has_perm('djangocbv.publisher_access') :
            return qs
        return qs.exclude(status='REMOVED')


class ModerationMixin:
    def form_valid(self, form):
        if self.object.status != 'REMOVED':
            if self.request.user.has_perm('djangocbv.publisher_access') or self.request.user.has_perm('djangocbv.admin_access'):
                self.object.status = 'PUBLISHED'
            else:
                self.object.status = 'DRAFT'

        return super().form_valid(form)


class SetInitialMixin(object,):
    def get_initial(self):
        initial = super(SetInitialMixin, self).get_initial()
        initial.update(self.request.GET.dict())
        return initial


class SuccessMessagesMixin(object, ):
    success_message = ''

    def get_success_message(self):
        return self.success_message

    def form_valid(self, form):
        messages.success(self.request, self.get_success_message())
        return super().form_valid(form)


class AnyPermissionRequiredMixin(UserPassesTestMixin):
    permissions = []

    def test_func(self):
        for p in self.permissions:
            if self.request.user.has_perm(p):
                return True
        return False


class AdminOrPublisherPermissionRequiredMixin(AnyPermissionRequiredMixin):
    permissions = ['djangocbv.admin_access', 'djangocbv.publisher_access']


class RequestArgMixin:
    def get_form_kwargs(self):
        kwargs = super(RequestArgMixin, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class RedirectToHomeMixin:
    def get_success_url(self):
        return reverse('home_django')


class RedirectToArticlesMixin:
    def get_success_url(self):
        return reverse('article-list')


class RedirectToDocumentsMixin:
    def get_success_url(self):
        return reverse('document-list')


class CreateSuccessMessageMixin(SuccessMessagesMixin):
    success_message = 'Object successfully created!'


class UpdateSuccessMessageMixin(SuccessMessagesMixin):
    success_message = 'Object successfully updated!'


class RemoveSuccessMessageMixin(SuccessMessagesMixin):
    success_message = 'Object successfully removed!'


class UnpublishSuccessMessageMixin(SuccessMessagesMixin):
    success_message = 'Object successfully unpublished!'

    
class CategoriesContextMixin:
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        return ctx    
    

class AddFilterMixin:
    filter_class = None
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if not self.filter_class:
            raise NotImplementedError("Please define filter_class when using AddFilterMixin")
        filter = self.filter_class(self.request.GET, queryset=self.get_queryset())
        ctx['filter'] = filter
        ctx[self.context_object_name] = filter.qs
        return ctx


class ExportCsvMixin:
    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('csv'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="export.csv"'

            writer = csv.writer(response)
            for idx, o in enumerate(context['object_list']):
                if idx == 0: # Write headers
                    writer.writerow(k for (k,v) in o.__dict__.items() if not k.startswith('_'))
                writer.writerow(v for (k,v) in o.__dict__.items() if not k.startswith('_'))

            return response
        return super().render_to_response(context, **response_kwargs)
        
        
class JsonDetailMixin:
    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('json'):
            response = HttpResponse(content_type='application/json')
            response.write(json.dumps(dict( (k,str(v)) for k,v in self.object.__dict__.items() )))
            return response
        return super().render_to_response(context, **response_kwargs)        


class SetOwnerIfNeeded:
    def form_valid(self, form, ):
        if not form.instance.owned_by_id:
            form.instance.owned_by = self.request.user
        return super().form_valid(form)


class RemoveMixin:
    def form_valid(self, form, ):
        form.instance.status = 'REMOVED'
        return super().form_valid(form)


class UnpublishMixin:
    def form_valid(self, form, ):
        form.instance.status = 'DRAFT'
        return super().form_valid(form)


class ContentCreateMixin(CreateSuccessMessageMixin,
                        AuditableMixin,
                        SetOwnerIfNeeded,
                        RequestArgMixin,
                        SetInitialMixin,
                        ModerationMixin,
                        LoginRequiredMixin):
    pass


class ContentUpdateMixin(UpdateSuccessMessageMixin,
                        AuditableMixin,
                        SetOwnerIfNeeded,
                        RequestArgMixin,
                        SetInitialMixin,
                        ModerationMixin,
                        LimitAccessMixin,
                        LoginRequiredMixin):
    pass


class ContentListMixin(ExportCsvMixin, AddFilterMixin, HideRemovedMixin, ):
    pass


class ContentRemoveMixin(AdminOrPublisherPermissionRequiredMixin,
                         AuditableMixin,
                         RemoveSuccessMessageMixin,
                         HideRemovedMixin,
                         RemoveMixin,):
    http_method_names = ['post',]
    fields = []


class ContentUnpublishMixin(AdminOrPublisherPermissionRequiredMixin,
                            AuditableMixin,
                            UnpublishSuccessMessageMixin,
                            UnpublishMixin,):
    http_method_names = ['post',]
    fields = []

    