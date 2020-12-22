import logging

from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from snippet.forms import SnippetForm
from snippet.models.snippet import Snippet

log = logging.getLogger(__name__)


class SnippetView(DetailView):
    template_name = 'snippet/snippet.html'
    model = Snippet
    context_object_name = 'snippet'


class AddSnippet(CreateView):
    template_name = 'snippet/add_snippet.html'
    context_object_name = 'snippet'
    model = Snippet
    form_class = SnippetForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateSnippet(UpdateView):
    template_name = 'snippet/update_snippet.html'
    context_object_name = 'snippet'
    model = Snippet
    form_class = SnippetForm

    def get_success_url(self):
        context = self.get_context_data()
        snippet = context['snippet']
        return snippet.get_absolute_url()


class DeleteSnippet(DeleteView):
    template_name = 'snippet/delete_snippet.html'
    model = Snippet
    success_url = reverse_lazy('snippet:home')
