from django.contrib.auth import mixins
from django.shortcuts import redirect


class BootstrapFormControlMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''

            field.widget.attrs['class'] += 'form-control'


class BookAccessMixin(mixins.PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('error')
        return super().dispatch(request, *args, **kwargs)


class UserAccessMixin(mixins.LoginRequiredMixin):
    kwargs = {}

    def dispatch(self, request, *args, **kwargs):
        if not request.user.pk == self.kwargs['pk']:
            return redirect('error')
        return super().dispatch(request, *args, **kwargs)
