from django.urls import path, re_path
from .import views
from django.contrib.auth.decorators import login_required
app_name = 'properties'


urlpatterns = [
	path('', views.properties, name="properties"),
	path('add-property/', login_required(views.addproperty), name='addproperty'),
	re_path('categories/(?P<slug>[\w-]+)/', views.categories, name='categories'),
	re_path('edit/(?P<slug>[\w-]+)/', views.editProperty, name='edit'),
	re_path('delete/(?P<slug>[\w-]+)/', views.propertyDelete, name='delete'),
	re_path('unavailable/(?P<slug>[\w-]+)/', views.unavailable, name='unavailable'),
	re_path('(?P<slug>[\w-]+)/publish/', views.publish, name='publish'),
	re_path('(?P<slug>[\w-]+)/', views.property, name='property'),
]