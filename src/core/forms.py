from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from account.models import UserProfile


class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}))

    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name", "phone_number", "birth_date", "city", "password1", "password2")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["gender", "user_type", "bio", "favourite_genres", "website", "postcode"]
