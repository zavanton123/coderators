from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from snippet.forms.tag_forms import TagForm
from snippet.models.tag_models import Tag


class ShowTags(ListView):
    template_name = 'snippet/tag/show_tags.html'
    model = Tag
    context_object_name = 'tags'


class ShowTag(DetailView):
    template_name = 'snippet/tag/show_tag.html'
    context_object_name = 'tag'
    model = Tag


class AddTag(CreateView):
    template_name = 'snippet/tag/add_tag.html'
    form_class = TagForm
    success_url = reverse_lazy('snippet:home')
    model = Tag


class UpdateTag(UpdateView):
    template_name = 'snippet/tag/update_tag.html'
    success_url = reverse_lazy('snippet:show_tags')
    form_class = TagForm
    model = Tag


class DeleteTag(DeleteView):
    model = Tag
    success_url = reverse_lazy('snippet:show_tags')
    template_name = 'snippet/tag/delete_tag.html'
