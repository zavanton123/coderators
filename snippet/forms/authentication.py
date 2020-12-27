from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# todo zavanton - add form localization
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


class LoginForm(AuthenticationForm):
    email = forms.EmailField(
        required=False,
        label="Email:",
        widget=forms.EmailInput(),
    )
    username = forms.CharField(
        label='Username:',
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput()
    )
