from django.urls import path

from core.views import (ActivateUser, IndexView, UserLogin, UserLogout,
                        UserProfile, UserRegistration)

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login/", UserLogin.as_view(), name="login"),
    path("user-profile/", UserProfile.as_view(), name="user_profile"),
    path("registration/", UserRegistration.as_view(), name="registration"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("activate/<str:uuid64>/<str:token>/", ActivateUser.as_view(), name="activate_user"),
]
