import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from apps.snippet.forms.tag_forms import TagForm
from apps.snippet.models.tag_models import Tag

log = logging.getLogger(__name__)


class ShowTags(ListView):
    template_name = 'snippet/tag/show_tags.html'
    model = Tag
    context_object_name = 'tags'


class ShowTag(DetailView):
    template_name = 'snippet/tag/show_tag.html'
    context_object_name = 'tag'
    model = Tag

    def dispatch(self, request, *args, **kwargs):
        path = request.get_full_path()
        log.debug(f'zavanton - path: {path}')
        return super().dispatch(request, *args, **kwargs)


class AddTag(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('authentication:login')
    redirect_field_name = 'next'
    template_name = 'snippet/tag/add_tag.html'
    form_class = TagForm
    success_url = reverse_lazy('snippet:home')
    model = Tag


class UpdateTag(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('authentication:login')
    redirect_field_name = 'next'
    template_name = 'snippet/tag/update_tag.html'
    success_url = reverse_lazy('snippet:show_tags')
    form_class = TagForm
    model = Tag


class DeleteTag(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('authentication:login')
    redirect_field_name = 'next'
    model = Tag
    success_url = reverse_lazy('snippet:show_tags')
    template_name = 'snippet/tag/delete_tag.html'
