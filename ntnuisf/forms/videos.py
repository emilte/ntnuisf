# imports
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from ..models.songs import Tag
from ..models.videos import Video, DIFFICULY_CHOISES
# End: imports -----------------------------------------------------------------


class VideoFilterForm(forms.Form):
    search = forms.CharField(required=False, label='Søk')
    tag = forms.ChoiceField(required=False)
    difficulty = forms.ChoiceField(required=False, label='Vanskelighetsgrad')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs.update({'class': 'video-search-filter form-control', 'placeholder': 'Søk...', 'autofocus': True})

        self.fields['tag'].choices = [(-1, '-----')]
        self.fields['tag'].choices += [(tag.id, tag.title) for tag in Tag.get_queryset(['video'])]
        self.fields['tag'].widget.attrs.update({'class': 'video-search-filter form-control'})

        self.fields['difficulty'].choices = [(-1, '-----')]
        self.fields['difficulty'].choices += DIFFICULY_CHOISES
        self.fields['difficulty'].widget.attrs.update({'class': 'video-search-filter form-control'})


class VideoForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.get_queryset(['video']), widget=FilteredSelectMultiple(verbose_name='tags', is_stacked=False), required=False
    )
    #difficulty = forms.ChoiceField(choices=())

    required_css_class = 'required font-bold'

    class Meta:
        model = Video
        fields = ['title', 'youtube_URL', 'embedded', 'tags', 'description', 'focus', 'difficulty']

    class Media:
        css = {
            'all': ['admin/css/widgets.css'],  # 'css/uid-manage-form.css'
        }
        # Adding this javascript is crucial
        js = ['/admin/jsi18n/']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
