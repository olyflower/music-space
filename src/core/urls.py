from django.urls import path

from core.views import (ActivateUser, EditUserProfileView, GetUserProfile,
                        IndexView, UserLogin, UserLogout, UserRegistration)

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login/", UserLogin.as_view(), name="login"),
    path("user-profile/", GetUserProfile.as_view(), name="user_profile"),
    path("edit-user-profile/<int:pk>/", EditUserProfileView.as_view(), name="edit_user_profile"),
    path("registration/", UserRegistration.as_view(), name="registration"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("activate/<str:uuid64>/<str:token>/", ActivateUser.as_view(), name="activate_user"),
]
