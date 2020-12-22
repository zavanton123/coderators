import logging

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from snippet.forms import RegisterForm

log = logging.getLogger(__name__)


class UserLoginView(LoginView):
    template_name = 'snippet/authentication/login.html'
    authentication_form = AuthenticationForm
    redirect_field_name = 'next'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('snippet:home')


class UserLogoutView(LogoutView):
    redirect_field_name = 'next'
    next_page = 'snippet:login'


class UserPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'snippet/authentication/user_password_change.html'

    def get_success_url(self):
        return reverse('snippet:password_change_done')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'snippet/authentication/user_password_change_done.html'


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'snippet/authentication/register.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrats! You have registered!')
            return redirect('snippet:login')
        else:
            messages.error(request, "Epic fail! You haven't registered yet!")
            form = RegisterForm()
            return render(request, 'snippet/authentication/register.html', context={'form': form})


class ProfileView(TemplateView):
    template_name = 'snippet/authentication/profile.html'
