from django import forms
from django.utils.translation import gettext_lazy as _

from apps.snippet.models import Snippet


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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 30%'
            }),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'style': 'max-width: 30%'
                })
        }
