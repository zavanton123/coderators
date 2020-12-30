from django import forms
from django.utils.translation import gettext_lazy as _

from snippet.models.category_models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        localized_fields = ('name', 'slug')
        labels = {'name': _('Name'), 'slug': _('Slug')}
