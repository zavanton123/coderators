from django import forms

from snippet.models.category import Category


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
