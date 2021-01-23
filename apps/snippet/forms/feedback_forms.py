from captcha.fields import CaptchaField
from django import forms

from django.utils.translation import gettext_lazy as _


class FeedbackForm(forms.Form):
    email = forms.EmailField(
        label=_('Email'),
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        localize=True,
    )
    subject = forms.CharField(
        label=_('Subject'),
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        localize=True,
    )
    content = forms.CharField(
        label=_('Content'),
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'rows': 10,
                'class': 'form-control',
            }
        ),
        localize=True,
    )
    captcha = CaptchaField()
