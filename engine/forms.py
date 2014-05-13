from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField

	def clean_email(self):
		email = self.cleaned_data.get('email')

		if not User.objects.filter(email=email).exists():
			raise form.ValidationError('Email address not found')

		return email


