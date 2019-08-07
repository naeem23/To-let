from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddPropertyForm, PropertyEditForm
from .models import Category, Property, Rating
from django.http import HttpResponseNotFound
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib import messages
from django.db.models import Sum
import math




def properties(request):
	property_list = Property.objects.active().order_by('-creation_date')

	if request.user.is_staff or request.user.is_superuser:
		property_list = Property.objects.all().order_by('-creation_date')

	query = request.GET.get("l")
	query1 = request.GET.get("t")
	query2 = request.GET.get("p")

	if query or query1 or query2: 
		property_list = property_list.filter(
			Q(location__icontains=query) &
			Q(category__name__icontains=query1) &
			Q(price__icontains=query2)
			).distinct()

		if property_list:
			paginator = Paginator(property_list, 3)
			page = request.GET.get('page')
			properties = paginator.get_page(page)
			
			context = {
				'p': properties,
			}
			return render(request, 'properties/properties.html', context)
		else:
			messages.error(request, 'No search result found.')


	paginator = Paginator(property_list, 6)
	page = request.GET.get('page')
	properties = paginator.get_page(page)
	
	context = {
		'p': properties,
	}
	return render(request, 'properties/properties.html', context)


def property(request, slug):
	instace = get_object_or_404(Property, slug=slug) 

	if instace.draft:
		if not request.user.is_staff:
			return HttpResponseNotFound()

	if request.method=="POST":
		rating = request.POST.get("rating")
		rate = Rating(property=instace, rating=rating)
		rate.save()

		all_rating = Rating.objects.filter(property=instace).count()
		all_rating_sum = Rating.objects.filter(property=instace).aggregate(Sum('rating'))

		all_rating_sum = all_rating_sum['rating__sum']

		avg_rating = math.ceil(all_rating_sum / all_rating)

		instace.rating = avg_rating
		print(instace.rating)
		instace.save()


	context = {
		'p': instace,
	}
	return render(request, 'properties/property.html', context)


def publish(request,slug):
    instance = get_object_or_404(Property, slug=slug)

    if instance.draft == True:
        instance.draft = False
        instance.save()
        return redirect('accounts:properties', username=request.user.username)


def unavailable(request,slug):
	instance = get_object_or_404(Property, slug=slug)

	if instance.is_available == True:
		instance.is_available = False
		instance.save()
		return redirect('accounts:profile', username=request.user.username)


def propertyDelete(request, slug):
	Property.objects.filter(slug=slug).delete()
	return redirect('accounts:profile', username=request.user.username)


def addproperty(request):
	if request.method == 'POST':
		form = AddPropertyForm(request.POST or None, request.FILES)

		if form.is_valid():
			add = form.addProperty()
			category = request.POST.get('cat')
			category_object = Category.objects.get(id=category) 
			add.save()
			add.category=category_object
			add.save()
			add.created_by = request.user.username
			add.save()
			return redirect('home:home')

	else:
		form = AddPropertyForm()

		cat = Category.objects.all().order_by('name')
		context = {
			'form': form,
			'cat': cat
		}

	return render(request, 'properties/addproperty.html', context)


def editProperty(request, slug):
	instance = get_object_or_404(Property, slug=slug)

	if request.POST:
		editform = PropertyEditForm(request.POST or None, request.FILES, instance=instance)

		if editform.is_valid():
			editform.save()

			return redirect('properties:property', slug=slug)
	else:
		editform = PropertyEditForm(instance=instance)

	context = {
		'form': editform,
	}

	return render(request, 'properties/editproperty.html', context)


def categories(request, slug):
	cat = get_object_or_404(Category, slug=slug)
	properties = Property.objects.filter(category=cat)

	context = {
		'c': cat,
		'properties': properties 
	}

	return render(request, 'properties/category.html', context)