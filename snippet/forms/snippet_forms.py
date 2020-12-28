from django import forms

from snippet.models import Snippet


# todo zavanton - add form localization
class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'content', 'category', 'tags']
