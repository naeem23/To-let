from django.shortcuts import render
from properties.models import Category, Property

def home(request):
	properties = Property.objects.active().order_by('-creation_date')[:6]

	if request.user.is_staff or request.user.is_superuser:
		properties = Property.objects.all().order_by('-creation_date')[:6]

	countA = Property.objects.filter(category__name__exact = 'Apartment').count()
	countH = Property.objects.filter(category__name__exact = 'House').count()
	countO = Property.objects.filter(category__name__exact = 'Office').count()


	context = {
		'p': properties,
		'countA': countA,
		'countH': countH,
		'countO': countO,
	}
	return render(request, 'home/home.html', context)