from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView, CreateView, DeleteView, UpdateView, RedirectView

from snippet.forms import SnippetForm, RegisterForm, LoginForm
from snippet.models import Snippet


class IndexView(TemplateView):
    template_name = 'snippet/index.html'


class AboutView(TemplateView):
    template_name = 'snippet/about.html'


class ClientView(TemplateView):
    template_name = 'snippet/clients.html'


class ContactsView(TemplateView):
    template_name = 'snippet/contact.html'


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'snippet/login.html', context={'form': form})

    def post(self, request):
        print("post is called")
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.get_user()
            login(request, user)
            return redirect('snippet:home')
        else:
            print("form is invalid")
            messages.error(request, 'Something is wrong! You have failed to log in!')
            form = LoginForm()
            return render(request, 'snippet/login.html', context={'form': form})


class LogoutView(RedirectView):
    url = reverse_lazy('snippet:home')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have logged out!')
        return super().dispatch(request, *args, **kwargs)


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'snippet/register.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrats! You have registered!')
            return redirect('snippet:login')
        else:
            messages.error(request, "Epic fail! You haven't registered yet!")
            form = RegisterForm()
            return render(request, 'snippet/register.html', context={'form': form})


class ProfileView(TemplateView):
    template_name = 'snippet/profile.html'


class AddSnippet(CreateView):
    form_class = SnippetForm
    context_object_name = 'snippet'
    model = Snippet
    template_name = 'snippet/add_snippet.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteSnippet(DeleteView):
    model = Snippet
    template_name = 'snippet/delete_snippet.html'
    success_url = reverse_lazy('snippet:home')


class EditSnippet(UpdateView):
    context_object_name = 'snippet'
    model = Snippet
    template_name = 'snippet/edit_snippet.html'
    fields = ['title', 'content']

    def get_success_url(self):
        context = self.get_context_data()
        snippet = context['snippet']
        return snippet.get_absolute_url()


class HomeView(ListView):
    ordering = ['-published_at']
    context_object_name = 'snippets'
    model = Snippet
    template_name = 'snippet/home.html'


class SnippetView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippet/snippet.html'
