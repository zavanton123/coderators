from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from snippet.models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'content']


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Username:',
        widget=forms.TextInput()
    )
    password1 = forms.CharField(
        label='Enter password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput()
    )
    email = forms.EmailField(
        label='Email:',
        widget=forms.EmailInput()
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
