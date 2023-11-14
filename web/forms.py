# --------------------------------------------------------------------------- #
# Django exceptions
from captcha.fields import CaptchaField, CaptchaTextInput, CaptchaAnswerInput
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
# --------------------------------------------------------------------------- #
# Models
from .models import FurnitureModel, UserModel, ContactUSModel, ColorsModel, faqModel
# --------------------------------------------------------------------------- #
# Translation
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# FAQ Model Form
class faqModelForm(forms.ModelForm):
    class Meta:
        model = faqModel
        fields = ['question', 'answer']


# --------------------------------------------------------------------------- #
# Furniture Model Form
class FurnitureModelForm(forms.ModelForm):
    class Meta:
        model = FurnitureModel
        exclude = ('created_at', 'updated_at', 'user')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Contact us Model Form

class ContactModelForm(forms.ModelForm):
    captcha = CaptchaField(widget=CaptchaTextInput(attrs=
    {
        'placeholder': _('Solve a math task...'),
        'class': 'captcha-input'
    }))

    class Meta:
        model = ContactUSModel
        exclude = ('created_at', 'updated_at', 'user')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Enter your name'),
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': _('Enter your email'),
            }),
            'message': forms.EmailInput(attrs={
                'placeholder': _('Enter your message'),
            })
        }


# --------------------------------------------------------------------------- #
# User Model Form
class AccountForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'phone', 'user_image', 'bio', 'telegram_username',
                  'github_username', 'twitter_username', 'instagram_username']


# --------------------------------------------------------------------------- #
# Login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
        'placeholder': _('Enter your username')
    }))

    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'placeholder': _('Enter you password')
    }))

    class Meta:
        model = UserModel
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


# --------------------------------------------------------------------------- #
# Registration
class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Passwords do not same')
        return self.cleaned_data['confirm_password']

    def clean_username(self):
        try:
            user = UserModel.objects.get(username=self.cleaned_data['username'])
            if user:
                raise ValidationError('This username is already in use')
        except:
            return self.cleaned_data['username']


# --------------------------------------------------------------------------- #
# Colors Model Form
class ColorForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'color'
    }))

    class Meta:
        model = ColorsModel
        fields = ['name', ]
# --------------------------------------------------------------------------- #
