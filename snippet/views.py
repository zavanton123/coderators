from django.views.generic import DetailView, ListView, TemplateView, CreateView

from snippet.forms import SnippetForm
from snippet.models import Snippet


class IndexView(TemplateView):
    template_name = 'snippet/index.html'


class AboutView(TemplateView):
    template_name = 'snippet/about.html'


class ClientView(TemplateView):
    template_name = 'snippet/clients.html'


class ContactsView(TemplateView):
    template_name = 'snippet/contact.html'


class LoginView(TemplateView):
    template_name = 'snippet/login.html'


class LogoutView(TemplateView):
    template_name = 'snippet/logout.html'


class RegisterView(TemplateView):
    template_name = 'snippet/register.html'


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


class HomeView(ListView):
    ordering = ['-published_at']
    context_object_name = 'snippets'
    model = Snippet
    template_name = 'snippet/home.html'


class SnippetView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippet/snippet.html'
