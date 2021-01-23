from django import forms
from django.utils.translation import get_language, gettext_lazy as _

from coderators import settings


class ChooseLanguageForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ChooseLanguageForm, self).__init__(*args, **kwargs)
        self.initial['language'] = get_language()

    language = forms.ChoiceField(
        label=_('Language'),
        choices=settings.LANGUAGES,
        widget=forms.RadioSelect(),
        localize=True
    )
