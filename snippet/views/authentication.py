from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import RedirectView, TemplateView

from snippet.forms import LoginForm, RegisterForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'snippet/authentication/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('snippet:home')
        else:
            messages.error(request, 'Something is wrong! You have failed to log in!')
            form = LoginForm()
            return render(request, 'snippet/authentication/login.html', context={'form': form})


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