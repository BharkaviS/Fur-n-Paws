from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account has been succesfully created for {username}! You can now login!')
			return redirect('login')
			def clean_username(self, username):
				user_model = get_user_model() # your way of getting the User
				try:
					user_model.objects.get(username__iexact=username)
				except user_model.DoesNotExist:
					return username
					raise forms.ValidationError(_("This username has already existed."))
	else:
		form = UserRegisterForm()

	return render(request,'users/register.html',{'form':form})

def About(request):
	return render(request,'users/about.html')

@login_required
def profile(request,):
	return render(request,'users/profile.html')
