from django import forms
from django.utils.translation import gettext_lazy as _

from apps.authentication.auth_models import CustomUser


class UpdateUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'style': 'max-width: 50%',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'style': 'max-width: 50%',
        })
        self.fields['experience'].widget.attrs.update({
            'class': 'form-control',
            'style': 'max-width: 50%',
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'rows': 5,
        })

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'experience',
            'description',
        ]
        localized_fields = [
            'first_name',
            'last_name',
            'experience',
            'description',
        ]
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'experience': _('Experience'),
            'description': _('Description'),
        }


class SetAvatarForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control',
            'style': 'max-width: 50%'
        })

    avatar = forms.ImageField(
        label=_('Avatar'),
        localize=True
    )
