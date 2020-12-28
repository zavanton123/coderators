from captcha.fields import CaptchaField
from django import forms


# todo zavanton - add form localization
class FeedbackForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(),
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(),
    )
    content = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={'rows': 10}
        ),
    )
    captcha = CaptchaField()