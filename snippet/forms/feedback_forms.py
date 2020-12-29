from captcha.fields import CaptchaField
from django import forms

# todo zavanton - add form localization
from django.utils.translation import gettext_lazy as _


class FeedbackForm(forms.Form):
    email = forms.EmailField(
        label=_('Email'),
        max_length=100,
        widget=forms.EmailInput(),
        localize=True,
    )
    subject = forms.CharField(
        label=_('Subject'),
        max_length=100,
        widget=forms.TextInput(),
        localize=True,
    )
    content = forms.CharField(
        label=_('Content'),
        max_length=1000,
        widget=forms.Textarea(
            attrs={'rows': 10}
        ),
        localize=True,
    )
    captcha = CaptchaField()
