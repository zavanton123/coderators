import logging

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View

from apps.authentication.auth_forms import RegisterForm

log = logging.getLogger(__name__)


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'authentication/auth/register.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrats! You have registered!')
            return redirect('snippet:login')
        else:
            messages.error(request, "Epic fail! You haven't registered yet!")
            form = RegisterForm()
            return render(request, 'authentication/auth/register.html', context={'form': form})


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_field_name = 'redirect_to'
    redirect_authenticated_user = True
    template_name = 'authentication/auth/login.html'

    # in the simple case (if we are not redirected to the login page from any other page)
    # go to the home url after successful login
    def get_redirect_url(self):
        redirect_url = super().get_redirect_url()
        if not redirect_url:
            redirect_url = reverse_lazy('snippet:home')
        return redirect_url


class UserLogoutView(LogoutView):
    redirect_field_name = 'redirect_to'
    next_page = 'snippet:login'


class UserPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'authentication/auth/user_password_change.html'

    def get_success_url(self):
        return reverse('snippet:password_change_done')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'authentication/auth/user_password_change_done.html'


class UserPasswordResetView(PasswordResetView):
    template_name = 'authentication/auth/user_password_reset.html'
    form_class = PasswordResetForm
    from_email = 'zavialov2010@gmail.com'
    email_template_name = 'snippet/auth/user_password_reset_email.html'

    def get_success_url(self):
        return reverse('snippet:password_reset_done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authentication/auth/user_password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/auth/user_password_reset_confirm.html'
    form_class = SetPasswordForm
    post_reset_login = False

    def get_success_url(self):
        return reverse('snippet:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'authentication/auth/user_password_reset_complete.html'
