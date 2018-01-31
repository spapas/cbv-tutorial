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
