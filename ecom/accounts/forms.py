from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

from ecom.accounts.models import SiteUser


class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=20,
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            return ValidationError('Email and/or password is incorrect.')

    def save(self):
        return self.user


class RegisterForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ('email',)