# imports
import typing
from http import HTTPStatus

from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from . import forms
from . import models

User = get_user_model()

if typing.TYPE_CHECKING:
    from django.http import HttpRequest
# End: imports -----------------------------------------------------------------


@method_decorator([login_required], name='dispatch')
class ExampleView(View):
    template = 'app_skeleton/example.html'
    form_class = forms.ExampleForm

    @permission_required('view_example')
    def get(self, request: HttpRequest, example_id: int, *args, **kwargs):
        example = get_object_or_404(models.Example, id=example_id)
        return render(request, self.template, {'example': example})

    @permission_required(['create_example', 'change_example'])
    def post(self, request: HttpRequest, example_id: int = None, *args, **kwargs):
        example = None
        if example_id:
            example = get_object_or_404(models.Example, id=example_id)
        form = self.form_class(data=request.POST, instance=example)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
            # return redirect('index')
        return render(request, self.template, {'form': form})

    @permission_required('delete_example')
    def delete(self, request: HttpRequest, example_id: int, *args, **kwargs):
        example = get_object_or_404(models.Example, id=example_id)
        example.delete()
        return HttpResponse(status=HTTPStatus.OK)
