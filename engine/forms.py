from django import forms
from django.contrib.auth.models import User

from passwords.fields import PasswordField


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control', 'type': 'email'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email address not found')

        return email


class SignupForm(forms.Form):
    email = forms.EmailField(required=True, max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control', 'type': 'email'}))
    password = PasswordField(required=True, max_length=200,
                             widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    first_name = forms.CharField(required=True, max_length=100,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
