# imports
from django_select2 import forms as select2_forms

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple

from ..models.songs import Tag
from ..models.courses import Course, CourseSection

User = get_user_model()

# End: imports -----------------------------------------------------------------

DATE_FORMATS = [
    '%d-%m-%y',
    '%d-%m-%Y',  # 26-02-97  26-02-1997
    '%d/%m/%y',
    '%d/%m/%Y',  # 26/02/97  26/02/1997
    '%d:%m:%y',
    '%d:%m:%Y',  # 26:02:97  26:02:1997
    '%d.%m.%y',
    '%d.%m.%Y',  # 26.02.97  26.02.1997
    '%d,%m,%y',
    '%d,%m,%Y',  # 26,02,97  26,02,1997
    '%d/%m-%y',
    '%d/%m-%Y',  # 26/02-97  26/02-1997
    '%d %m %y',
    '%d %m %Y',  # 26 02 97  26 02 1997
]

TIME_FORMATS = [
    '%H:%M',  # '14:30'
    '%H.%M',  # '14.30'
    '%H %M',  # '14 30'
]

MIN_FORMATS = ['%M']


class CourseForm(forms.ModelForm):
    q = Tag.get_queryset(['course'])

    tags = forms.ModelMultipleChoiceField(queryset=q, widget=FilteredSelectMultiple(verbose_name='tags', is_stacked=False), required=False)
    date = forms.DateField(input_formats=DATE_FORMATS, required=False, label='Dato')
    start = forms.DateTimeField(input_formats=TIME_FORMATS, required=False, label='Start')
    end = forms.DateTimeField(input_formats=TIME_FORMATS, required=False, label='Slutt')

    required_css_class = 'required font-bold'

    # instructors = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=select2_forms.Select2MultipleWidget)

    class Media:
        css = {
            'all': ['admin/css/widgets.css'],  # 'css/uid-manage-form.css'
        }
        # Adding this javascript is crucial
        js = ['/admin/jsi18n/']

    class Meta:
        model = Course
        fields = [
            'title',
            'place',
            'date',
            'start',
            'end',
            'lead',
            'follow',
            'comments',
            'tags',
            # 'instructors',
            'bulk',
            'day',
            'external',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # self.fields['external'].widget.attrs.update({'class': ''})

        self.fields['title'].widget.attrs.update({'placeholder': 'Tittel'})

        self.fields['start'].widget.attrs.update({'placeholder': 'hh:mm'})
        self.fields['start'].widget.format = '%H:%M'

        self.fields['date'].widget.attrs.update({'placeholder': 'dd.mm.yy'})
        self.fields['date'].widget.format = '%d.%m.%y'

        self.fields['end'].widget.attrs.update({'placeholder': 'hh:mm'})
        self.fields['end'].widget.format = '%H:%M'

        self.fields['comments'].widget.attrs.update({'rows': '7'})


class SectionForm(forms.ModelForm):
    # duration = forms.TimeField(input_formats=MIN_FORMATS, required=False)
    required_css_class = 'required font-bold'

    class Meta:
        model = CourseSection
        exclude = ['nr']  # pylint: disable=modelform-uses-exclude
        widgets = {
            'song': select2_forms.Select2Widget(),
            'song2': select2_forms.Select2Widget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['duration'].widget.attrs.update({'placeholder': 'min'})
        # self.fields['duration'].widget.format = '%M'

        self.fields['start'].widget.attrs.update({'placeholder': 'hh:mm', 'readonly': '1'})
        self.fields['start'].widget.format = '%H:%M'

        self.fields['description'].widget.attrs.update({'class': 'tinymce'})


class CourseFilterForm(forms.Form):
    search = forms.CharField(required=False, label='Søk')
    tag = forms.ChoiceField(required=False, widget=select2_forms.Select2Widget())
    # tag = forms.ChoiceField(required=False)
    lead = forms.ChoiceField(required=False, widget=select2_forms.Select2Widget(), label='Instruktør (lead)')
    # lead = forms.ChoiceField(required=False, label='Instruktør (lead)')
    follow = forms.ChoiceField(required=False, widget=select2_forms.Select2Widget(), label='Instruktør (follow)')
    bulk = forms.IntegerField(required=False, label='Bolk')
    day = forms.IntegerField(required=False, label='Dag')
    semester_char = forms.CharField(required=False, label='Semester')
    external = forms.BooleanField(initial=False, required=False, label='Eksternkurs')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # pass
            self.fields[field].widget.attrs.update({'class': 'course-filter form-control'})

        self.fields['external'].widget.attrs.update({'class': 'invisible'})

        self.fields['search'].widget.attrs.update({'placeholder': 'Søk på tittel...', 'autofocus': True})
        self.fields['semester_char'].widget.attrs.update({
            'placeholder': 'Eks: H2019, V2020',
        })

        # self.fields['tag'].choices = [(-1, '-----')]
        self.fields['tag'].choices += [(tag.id, tag.title) for tag in Tag.get_queryset(['course'])]
        self.fields['tag'].widget.attrs.update({'class': 'form-control course-filter'})

        # self.fields['lead'].choices = [(-1, '-----')]
        self.fields['lead'].choices += [(lead.id, lead) for lead in User.objects.all()]

        # self.fields['follow'].choices = [(-1, '-----')]
        self.fields['follow'].choices += [(follow.id, follow) for follow in User.objects.all()]
