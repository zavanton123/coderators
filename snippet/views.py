from django.views.generic import TemplateView, DetailView

from snippet.models import Snippet


class HomeView(TemplateView):
    template_name = 'snippet/home.html'


class SnippetView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippet/snippet.html'
