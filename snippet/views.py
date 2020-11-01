from django.views.generic import DetailView, ListView, TemplateView

from snippet.models import Snippet


class IndexView(TemplateView):
    template_name = 'snippet/index-template.html'


class AboutView(TemplateView):
    template_name = 'snippet/about-template.html'


class ClientView(TemplateView):
    template_name = 'snippet/clients-template.html'


class ContactView(TemplateView):
    template_name = 'snippet/contact-template.html'


class HomeView(ListView):
    ordering = ['-published_at']
    context_object_name = 'snippets'
    model = Snippet
    template_name = 'snippet/home.html'


class SnippetView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippet/snippet.html'
