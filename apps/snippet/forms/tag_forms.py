from django import forms
from django.utils.translation import gettext_lazy as _

from apps.snippet.models.tag_models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        labels = {'name': _('Name'), 'slug': _('Slug')}
        localized_fields = ['name', 'slug']
        fields = ['name', 'slug']
