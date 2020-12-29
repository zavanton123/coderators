from django import forms
from django.utils.translation import gettext_lazy as _

from snippet.models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'content', 'category', 'tags']
        labels = {
            'title': _('Title'),
            'content': _('Content'),
            'category': _('Category'),
            'tags': _('Tags'),
        }
        localized_fields = ['title', 'content', 'category', 'tags']
