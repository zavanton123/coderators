from django import forms
from django.utils.translation import gettext_lazy as _

from apps.snippet.models.tag_models import Tag


class TagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'style': 'max-width: 50%',
        })

    class Meta:
        model = Tag
        fields = ['name']
        localized_fields = ['name']
        labels = {'name': _('Name')}
