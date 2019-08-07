from django.contrib import admin
from .models import Category, Property, Rating

class CategoryAdmin(admin.ModelAdmin):
	ordering = ['name']
		
admin.site.register(Category, CategoryAdmin)
admin.site.register(Property)
admin.site.register(Rating)
