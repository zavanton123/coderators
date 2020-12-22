from django.urls import reverse_lazy
from django.views.generic import CreateView

from snippet.forms.tag import TagForm
from snippet.models.tag import Tag


class AddTag(CreateView):
    template_name = 'snippet/tag/add_tag.html'
    form_class = TagForm
    success_url = reverse_lazy('snippet:home')
    model = Tag
