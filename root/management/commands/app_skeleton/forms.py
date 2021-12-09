# imports
from django import forms
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()
# End: imports -----------------------------------------------------------------


class ExampleForm(forms.ModelForm):

    required_css_class = 'required font-bold'

    extra = forms.CheckboxInput()

    class Meta:
        model = models.Example
        fields = [
            'some',
            'thing',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
