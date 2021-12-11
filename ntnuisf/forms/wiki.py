# imports
from django import forms

from ..models.wiki import Folder, Page
# End: imports -----------------------------------------------------------------


class PageForm(forms.ModelForm):

    required_css_class = 'required font-bold'

    class Meta:
        model = Page
        fields = [
            'title',
            'folder',
            'content',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'tinymce'})
        # self.fields['private'].widget.attrs.update({'id': 'private-toggle'})


class FolderForm(forms.ModelForm):

    required_css_class = 'required font-bold'

    class Meta:
        model = Folder
        fields = [
            'title',
            'root_folder',
            'perm',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'placeholder': 'Tittel'})
