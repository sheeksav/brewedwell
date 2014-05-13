from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'type': 'email'}))
	password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

	def clean_email(self):
		email = self.cleaned_data.get('email')

		if not User.objects.filter(email=email).exists():
			raise forms.ValidationError('Email address not found')

		return email

