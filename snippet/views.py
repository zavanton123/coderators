from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, DeleteView, UpdateView

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
