from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(),
        localize=True,
    )
    password1 = forms.CharField(
        label=_('Enter password'),
        widget=forms.PasswordInput(),
        localize=True,
    )
    password2 = forms.CharField(
        label=_('Confirm password'),
        widget=forms.PasswordInput(),
        localize=True,
    )
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(),
        localize=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
