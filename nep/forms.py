from django import forms
from .models import User
class SignupForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Type password'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'name@gmail.com'}))


class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'username',
			'password',
		]

		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
		}

class ContactsForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'name@gmail.com'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message', 'rows':8}))