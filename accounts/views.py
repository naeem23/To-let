from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from properties.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contact.models import *

def signup_views(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			user = form.signup(request)
			user.save()
			return redirect('accounts:login')

	else:
		form = SignupForm()

	context = {
		'form': form,
	}

	return render(request, 'accounts/signup.html', context)



def login_view(request):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			user = form.login()
			login(request,user)
			return redirect('accounts:profile', username=request.user)
	else:
		form = LoginForm()

	context = {
		'form': form,
	}
	return render(request, 'accounts/login.html', context)


def logout_view(request):
	if request.method == 'POST':
		logout(request)

	return redirect('home:home')


def profile(request, username):
	user = get_object_or_404(User, username=username)

	property_list = Property.objects.filter(created_by=user).order_by('-creation_date')

	if request.user.is_staff or request.user.is_superuser:
		property_list = Property.objects.all().order_by('-creation_date')

	paginator = Paginator(property_list, 6)
	page = request.GET.get('page')
	properties = paginator.get_page(page)

	context = {
		'properties': properties,
	}

	return render(request, 'accounts/profile.html', context)
