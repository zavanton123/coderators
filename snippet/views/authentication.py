import logging

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import RedirectView, TemplateView

from snippet.forms import RegisterForm

log = logging.getLogger(__name__)


class MyLoginView(LoginView):
    template_name = 'snippet/authentication/login.html'
    authentication_form = AuthenticationForm
    redirect_field_name = 'next'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('snippet:home')


class LogoutView(RedirectView):
    url = reverse_lazy('snippet:home')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have logged out!')
        return super().dispatch(request, *args, **kwargs)


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
