from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class NewUserForm(forms.Form):
    
	name = forms.CharField(max_length=150)	
	password = forms.CharField(max_length=150, widget=forms.PasswordInput())	
	city = forms.CharField(max_length=150)
	age = forms.IntegerField()
    
	class Meta:
		model = Customer
		fields = ("name", "city","age")


class LoginForm(forms.Form):
	name = forms.CharField(max_length=150)	
	password = forms.CharField(max_length=150, widget=forms.PasswordInput())	
	class Meta:
		model = Customer
		fields = ("name")