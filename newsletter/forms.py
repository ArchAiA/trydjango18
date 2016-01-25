from django import forms
from .models import SignUp

class ContactForm(forms.Form):		#L15
	full_name = forms.CharField(required=False)	#L15
	email = forms.EmailField()		#L15
	message = forms.CharField()		#L15

#Over-riding the function to clean data
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .edu email address")
		return email




class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
		#exclude = ['full_name'] #Use Sparingly

#Over-riding the function to clean data
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .edu email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		return full_name 

