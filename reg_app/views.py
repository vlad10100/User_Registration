from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . forms import NewCreateUserForm


# Create your views here.

def home(request):
	return render(request, 'reg_app/home.html')
@login_required
def profile(request):
	return render(request, 'reg_app/profile.html')

def signup(request):
	form = NewCreateUserForm()
	context = {'form': form}
	if request.method == 'POST':
		form = NewCreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"Hi {username}, you have successfully created an account.")
			return login_page(request)
	else:
		form = NewCreateUserForm()
	return render(request, 'reg_app/signup.html', context)

def login_page(request):
	context = {}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			username = request.POST.get('username')
			messages.success(request, f"Hi {username}, you have successfully logged in.")
			return home(request)

	return render(request, 'reg_app/login.html')

def logout_page(request):
	logout(request)
	messages.success(request, f"You have been logged out.")
	return render(request, 'reg_app/logout_page.html')