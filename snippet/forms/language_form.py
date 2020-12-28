from django import forms
from django.utils.translation import get_language

from coderators import settings


class ChooseLanguageForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ChooseLanguageForm, self).__init__(*args, **kwargs)
        self.initial['language'] = get_language()

    language = forms.ChoiceField(
        choices=settings.LANGUAGES,
        widget=forms.RadioSelect()
    )
