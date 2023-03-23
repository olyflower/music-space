from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import (CreateView, RedirectView, TemplateView,
                                  UpdateView)

from account.models import UserProfile
from core.forms import UserProfileForm, UserRegistrationForm
from core.services.emails import send_registration_email
from core.utils.token_generator import TokenGenerator


class IndexView(TemplateView):
    template_name = "../templates/index.html"
    http_method_names = ["get"]
    extra_context = {"site_name": "Music-space"}


class UserLogin(LoginView):
    ...


class UserLogout(LogoutView):
    ...


class UserRegistration(CreateView):
    template_name = "registration/create_user.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()

        send_registration_email(request=self.request, user_instance=self.object)

        return super().form_valid(form)


class ActivateUser(RedirectView):
    url = reverse_lazy("core:index")

    def get(self, request, uuid64, token, *args, **kwargs):
        try:
            pk = force_str(urlsafe_base64_decode(uuid64))
            current_user = get_user_model().objects.get(pk=pk)
        except (ValueError, get_user_model().DoesNotExist, TypeError):
            return HttpResponse("Wrong data!!!")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()

            login(request, current_user)

            return super().get(request, *args, **kwargs)

        return HttpResponse("Wrong data!!!")


class GetUserProfile(TemplateView):
    template_name = "registration/user_profile.html"


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    login_url = "core:login"
    model = UserProfile
    form_class = UserProfileForm
    template_name = "registration/edit_user_profile.html"
    success_url = reverse_lazy("core:user_profile")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
