from django import forms

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


class SetAvatarForm(forms.Form):
    avatar = forms.ImageField()
