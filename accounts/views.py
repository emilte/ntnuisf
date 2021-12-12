# imports
import spotipy

from django.conf import settings
from django.http import HttpRequest
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import (
    login,
    logout,
    authenticate,
    get_user_model,
    update_session_auth_hash,
)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)

from ntnuisf.views import wiki as wiki_views

from . import (
    forms as account_forms,
    models as account_models,
)

User = get_user_model()
# End: imports -----------------------------------------------------------------


@method_decorator([login_required], name='dispatch')
class ProfileView(View):
    template = 'accounts/profile.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, self.template, {})


@method_decorator([login_required], name='dispatch')
class ProfileViewCopy(View):
    template = 'accounts/profile copy.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        courses = request.user.get_courses()
        return render(request, self.template, {'courses': courses})


@method_decorator([login_required], name='dispatch')
class EditProfileView(View):
    template = 'accounts/edit_profile.html'
    form_class = account_forms.EditUserForm

    def get(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template, {'form': form})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profilen din har blitt oppdatert')
            return redirect('accounts:profile')
        return render(request, self.template, {'form': form})


@method_decorator([login_required], name='dispatch')
class EditProfileViewCopy(View):
    template = 'accounts/edit_profile copy.html'
    form_class = account_forms.EditUserForm

    def get(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template, {'form': form})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        return render(request, self.template, {'form': form})


class SignUpView(View):
    template = 'accounts/registration_form.html'
    form_class = account_forms.SignUpForm

    def get(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            try:
                code = form.cleaned_data['code']
                group = account_models.PermissionCode.objects.get(secret=code).group
                user.groups.add(group)
                messages.success(request, f"Med koden '{code}' har du blitt lagt til i avdeling: {group.name}")
            except:  # pylint: disable=bare-except
                messages.warning(request, f"Koden '{code}' tilsvarer ingen avdeling. Ta kontakt med admin.")

            return redirect('home')
        return render(request, self.template, {'form': form})


@method_decorator([login_required], name='dispatch')
class DeleteUserView(View):

    def delete(self, request: HttpRequest, *args, **kwargs):
        request.user.delete()
        logout(request)
        messages.success(request, 'Brukeren din har blitt slettet fra systemet.')
        return redirect('home')


class LoginView(View):
    template = 'accounts/login.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, self.template)

    def post(self, request: HttpRequest, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        error = None
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        error = 'Feil'

        return render(request, self.template, {'error': error})


@method_decorator([login_required], name='dispatch')
class LogoutView(View):

    def get(self, request: HttpRequest, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')


@method_decorator([login_required], name='dispatch')
class ChangePasswordView(View):
    template = 'accounts/change_password.html'
    form_class = account_forms.CustomPasswordChangeForm

    def get(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request=request)
        return render(request, self.template, {'form': form})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(data=request.POST, request=request)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('accounts:profile')
        return render(request, self.template, {'form': form})


@method_decorator([login_required], name='dispatch')
class SettingsView(View):
    template = 'accounts/settings.html'
    form_class = account_forms.SettingsForm

    def get(self, request: HttpRequest, *args, **kwargs):
        user_settings, _created = account_models.Settings.objects.get_or_create(user=request.user)
        form = self.form_class(instance=user_settings, user=request.user)
        themes = form.fields['main_theme'].queryset

        return render(request, self.template, {'form': form, 'themes': themes})

    def post(self, request: HttpRequest, *args, **kwargs):
        user_settings, _created = account_models.Settings.objects.get_or_create(user=request.user)
        form = self.form_class(request.POST, instance=user_settings, user=request.user)
        themes = form.fields['main_theme'].queryset

        if form.is_valid():
            user_settings = form.save()
            return redirect('accounts:profile')
        return render(request, self.template, {'form': form, 'themes': themes})


@method_decorator([login_required, permission_required('accounts.add_theme', login_url='forbidden')], name='dispatch')
class AddTheme(wiki_views.GenericAddModel):
    template = 'accounts/theme_form.html'
    form_class = account_forms.ThemeForm
    redirect_name = 'accounts:settings'


@method_decorator([login_required, permission_required('accounts.change_theme', login_url='forbidden')], name='dispatch')
class EditTheme(wiki_views.GenericEditModel):
    template = 'accounts/theme_form.html'
    form_class = account_forms.ThemeForm
    redirect_name = 'accounts:settings'
    model = account_models.Theme

    def get(self, request: HttpRequest, model_id, *args, **kwargs):
        if request.user != self.model.objects.get(id=model_id).user:
            return redirect('forbidden')
        return super().get(request, model_id, *args, **kwargs)

    def post(self, request: HttpRequest, model_id, *args, **kwargs):
        if request.user != self.model.objects.get(id=model_id).user:
            return redirect('forbidden')
        return super().post(request, model_id, *args, **kwargs)


class SpotifyConnectView(View):
    template = 'accounts/spotify_connect.html'

    def post(self, request: HttpRequest, *args, **kwargs):

        cache_path = settings.SPOTIFY_CACHE_PATH + '.spotify-token-' + request.user.email
        sp_oauth = spotipy.SpotifyOAuth(
            settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_CLIENT_SECRET, settings.SPOTIFY_REDIRECT_URI, scope=settings.SPOTIFY_SCOPE, cache_path=cache_path
        )

        token_info = sp_oauth.get_cached_token()

        if not token_info:
            auth_url = sp_oauth.get_authorize_url()
            try:
                print(auth_url)
                import webbrowser  # pylint: disable=import-outside-toplevel
                webbrowser.open(auth_url + '&show_dialog=true')
            except Exception as e:  # pylint: disable=broad-except
                print(e)

        return redirect('accounts:profile')


def callback(request):
    response = request.build_absolute_uri()
    sp_oauth = spotipy.SpotifyOAuth(settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_CLIENT_SECRET, settings.SPOTIFY_REDIRECT_URI, scope=settings.SPOTIFY_SCOPE)

    sp_token, _created = account_models.SpotifyToken.objects.get_or_create(user=request.user)

    code = sp_oauth.parse_response_code(response)
    token_info = sp_oauth.get_access_token(code)
    sp_token.add_info(token_info)

    return redirect('accounts:profile')
