from django import forms

from snippet.models.tag import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
