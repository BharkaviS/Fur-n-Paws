from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	'''adress1 = forms.CharField()
	adress2 = forms.CharField()
	ladnmark = fomrs.CharField() 
	mobile.no = forms.IntegerField()'''


	class Meta:
		model = User 
		fields = ['username','email','password1','password2']