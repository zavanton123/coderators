from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput()
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
