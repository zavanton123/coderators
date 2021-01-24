from allauth.account.forms import SignupForm
from captcha.fields import CaptchaField

from apps.authentication.auth_models import CustomUser


class RegisterForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
