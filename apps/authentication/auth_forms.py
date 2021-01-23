from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from apps.authentication.auth_models import CustomUser


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
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
