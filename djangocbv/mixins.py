from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse
import csv


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
        return qs.filter(created_by=self.request.user)
        
        
class ModerationMixin:
    def form_valid(self, form):
        redirect_to = super().form_valid(form)
        if self.object.status != 'REMOVED':
            if self.request.user.has_perm('spots.publisher_access'):
                self.object.status = 'PUBLISHED'
            else:
                self.object.status = 'DRAFT'
            self.object.save()
            
        return redirect_to        


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


class CreateSuccessMessageMixin(SuccessMessagesMixin):
    success_message = 'Object successfully created!'


class UpdateSuccessMessageMixin(SuccessMessagesMixin):
    success_message = 'Object successfully updated!'


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



class SetOwnerIfNeeded:
    def form_valid(self, form, ):
        if not form.instance.owned_by_id:
            form.instance.owned_by = self.request.user
        return super().form_valid(form)
