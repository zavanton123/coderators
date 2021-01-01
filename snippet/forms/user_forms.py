from django import forms
from django.utils.translation import gettext_lazy as _

from snippet.models import CustomUser


class UpdateUserForm(forms.ModelForm):
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
    avatar = forms.ImageField(
        label=_('Avatar'),
        localize=True
    )
