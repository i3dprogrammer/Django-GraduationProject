from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from professorsApp.models import Professor

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())
	username.widget.attrs.update({'class':'form-control input-lg', 'placeholder':'Username'})
	password.widget.attrs.update({'class':'form-control input-lg', 'placeholder':'Password'})
	
class UserForm(ModelForm):

	first_name = forms.CharField(max_length=30, required=True)
	last_name = forms.CharField(max_length=30, required=True)
	
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name', 'email']
		widgets = {
			'password': forms.PasswordInput(),
		}
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exclude(username=username).exists():
			raise forms.ValidationError('Student with that e-mail address already exists.')
		return email
		
class RegisterProfessorForm(ModelForm):
	class Meta:
		model = Professor
		fields = ['info', 'image']