from django import forms

from snippet.models.category_models import Category


# todo zavanton - add form localization
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
