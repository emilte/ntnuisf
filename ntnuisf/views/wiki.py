# imports
from django.http import HttpRequest
from django.views import View
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from ..forms import wiki as wiki_forms
from ..models import wiki as wiki_models

# End: imports -----------------------------------------------------------------

# pylint: disable=all


class GenericAddModel(View):
    template = None  # (*) Required
    form_class = None  # (*)
    redirect_name = None  # (*)
    redirect_id = None
    success_msg = 'Lagringen var vellykket!'
    error_msg = 'Lagringen var misslykket!'

    def get(self, request: HttpRequest):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request: HttpRequest):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            try:
                obj.creator = request.user
            except Exception as e:  # pylint: disable=broad-except
                print(e)

            try:
                obj.created = timezone.now()
            except Exception as e:  # pylint: disable=broad-except
                print(e)

            try:
                obj.last_editor = request.user
            except Exception as e:  # pylint: disable=broad-except
                print(e)

            try:
                obj.last_edited = timezone.now()
            except Exception as e:  # pylint: disable=broad-except
                print(e)

            # Save
            obj.save()
            try:
                obj.save_m2m()
            except Exception as e:  # pylint: disable=broad-except
                print(e)

            messages.success(request, self.success_msg)

            if self.redirect_id:
                return redirect(self.redirect_name, getattr(obj, self.redirect_id))
            else:
                return redirect(self.redirect_name)
        else:
            messages.error(request, self.error_msg)
            return render(request, self.template, {'form': form})


class GenericEditModel(GenericAddModel):
    model = None  # Required

    def get(self, request: HttpRequest, model_id):
        instance = self.model.objects.get(id=model_id)
        form = self.form_class(instance=instance)
        return render(request, self.template, {'form': form, 'model_id': model_id})

    def post(self, request: HttpRequest, model_id):
        instance = self.model.objects.get(id=model_id)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                instance.last_editor = request.user
                instance.last_edited = timezone.now()
            except Exception as e:
                print(e)
            finally:
                instance.save()

            messages.success(request, self.success_msg)

            if self.redirect_id:
                return redirect(self.redirect_name, getattr(instance, self.redirect_id))
            else:
                return redirect(self.redirect_name)
        else:
            messages.error(request, self.error_msg)
            return render(request, self.template, {'form': form, 'model_id': model_id})


@method_decorator([login_required], name='dispatch')
class Dashboard(View):
    template = 'ntnuisf/wiki/dashboard2.html'

    def get(self, request: HttpRequest):
        # messages.info(request, 'OBS: Under utvikling')
        folders = wiki_models.Folder.objects.all()
        single_pages = wiki_models.Page.objects.filter(folder=None)
        root_folders = wiki_models.Folder.objects.filter(root_folder=None)  # (**) dashboard2

        return render(
            request,
            self.template,
            {
                'folders': folders,
                'single_pages': single_pages,
                'root_folders': root_folders,  # (**)
            }
        )


page_view_dec = [
    login_required,
    # permission_required('wiki.view_page', login_url='forbidden')
]


@method_decorator(page_view_dec, name='dispatch')
class PageView(View):
    template = 'ntnuisf/wiki/page_view3.html'

    def get(self, request: HttpRequest, model_id):

        page = wiki_models.Page.objects.get(id=model_id)

        for folder in page.root_path():
            if folder.perm:
                key = folder.perm.natural_key()
                perm_label = f'{key[1]}.{key[0]}'  # TODO: this must have an easier solution django....
                if not request.user.has_perm(perm_label):
                    return redirect('forbidden')

        # Needed for dashboard
        folders = wiki_models.Folder.objects.all()  # (*) dashboard
        single_pages = wiki_models.Page.objects.filter(folder=None)
        root_folders = wiki_models.Folder.objects.filter(root_folder=None)  # (**) dashboard2

        return render(
            request,
            self.template,
            {
                'page': page,
                'folders': folders,  # (*)
                'single_pages': single_pages,
                'root_folders': root_folders,  # (**)
            }
        )


@method_decorator([login_required, permission_required('wiki.create_page', login_url='forbidden')], name='dispatch')
class AddPage(GenericAddModel):
    template = 'ntnuisf/wiki/page_form.html'
    form_class = wiki_forms.PageForm
    redirect_name = 'ntnuisf:wiki:page_view'
    redirect_id = 'id'


@method_decorator([login_required, permission_required('wiki.change_page', login_url='forbidden')], name='dispatch')
class EditPage(GenericEditModel):
    template = 'ntnuisf/wiki/page_form.html'
    form_class = wiki_forms.PageForm
    redirect_name = 'ntnuisf:wiki:page_view'
    redirect_id = 'id'
    model = wiki_models.Page


@method_decorator([login_required, permission_required('wiki.create_folder', login_url='forbidden')], name='dispatch')
class AddFolder(GenericAddModel):
    template = 'ntnuisf/wiki/folder_form.html'
    form_class = wiki_forms.FolderForm
    redirect_name = 'ntnuisf:wiki:dashboard'


@method_decorator([login_required, permission_required('wiki.change_folder', login_url='forbidden')], name='dispatch')
class EditFolder(GenericEditModel):
    template = 'ntnuisf/wiki/folder_form.html'
    form_class = wiki_forms.FolderForm
    redirect_name = 'ntnuisf:wiki:dashboard'
    model = wiki_models.Folder
