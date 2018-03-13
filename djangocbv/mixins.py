from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse

class AuditableMixin:
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super().form_valid(form)


class LimitAccessMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_superuser:
            return qs
        return qs.filter(created_by=self.request.user)


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
    permissions = ['app.admin', 'app.publisher']


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