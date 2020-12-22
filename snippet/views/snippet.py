import logging

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from snippet.forms import SnippetForm
from snippet.models.snippet import Snippet
from snippet.models.tag import Tag

log = logging.getLogger(__name__)


class ShowSnippet(DetailView):
    template_name = 'snippet/snippet/show_snippet.html'
    model = Snippet
    context_object_name = 'snippet'


class AddSnippet(CreateView):
    template_name = 'snippet/snippet/add_snippet.html'
    context_object_name = 'snippet'
    model = Snippet
    form_class = SnippetForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateSnippet(UpdateView):
    template_name = 'snippet/snippet/update_snippet.html'
    context_object_name = 'snippet'
    model = Snippet
    form_class = SnippetForm

    def get_success_url(self):
        context = self.get_context_data()
        snippet = context['snippet']
        return snippet.get_absolute_url()


class DeleteSnippet(DeleteView):
    template_name = 'snippet/snippet/delete_snippet.html'
    model = Snippet
    success_url = reverse_lazy('snippet:home')


class ShowSnippetsByCategory(ListView):
    template_name = 'snippet/snippet/show_snippets.html'
    context_object_name = 'snippets'

    def get_queryset(self):
        search_category_id = self.kwargs['pk']
        return Snippet.objects.filter(category_id=search_category_id)


class ShowSnippetsByTag(ListView):
    template_name = 'snippet/snippet/show_snippets.html'
    context_object_name = 'snippets'
    model = Snippet

    def get_queryset(self):
        search_tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Snippet.objects.filter(tags__slug=search_tag.slug)
