from django import forms

from snippet.models.tag_models import Tag


# todo zavanton - add form localization
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
