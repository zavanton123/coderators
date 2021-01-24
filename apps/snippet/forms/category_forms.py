from django import forms

from apps.snippet.models.category_models import Category


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'style': 'max-width: 50%',
        })

    class Meta:
        model = Category
        fields = ['name']
        localized_fields = ['name']
