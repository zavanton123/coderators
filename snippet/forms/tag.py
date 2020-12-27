from django import forms

from snippet.models.tag import Tag


# todo zavanton - add form localization
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
