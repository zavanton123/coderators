import logging

from allauth.account.views import SignupView, LoginView, LogoutView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import reverse, reverse_lazy

from apps.authentication.auth_forms import RegisterForm, CustomLoginForm, CustomPasswordChangeForm, \
    CustomSetPasswordForm, CustomPasswordResetForm

log = logging.getLogger(__name__)


class RegisterView(SignupView):
    form_class = RegisterForm
    template_name = 'authentication/auth/register.html'


class UserLoginView(LoginView):
    template_name = 'authentication/auth/login.html'
    form_class = CustomLoginForm
    redirect_url = reverse_lazy('snippet:home')
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    template_name = 'authentication/auth/logout.html'


class UserPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'authentication/auth/user_password_change.html'

    def get_success_url(self):
        return reverse('authentication:password_change_done')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'authentication/auth/user_password_change_done.html'


class UserPasswordResetView(PasswordResetView):
    template_name = 'authentication/auth/user_password_reset.html'
    form_class = CustomPasswordResetForm
    from_email = 'zavialov2010@gmail.com'
    email_template_name = 'authentication/auth/user_password_reset_email.html'

    def get_success_url(self):
        return reverse('authentication:password_reset_done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authentication/auth/user_password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/auth/user_password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    post_reset_login = False

    def get_success_url(self):
        return reverse('authentication:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'authentication/auth/user_password_reset_complete.html'
