from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.timezone import now


class Category(models.Model):
	name = models.CharField(max_length=25, default='', blank=True)
	slug = models.SlugField(unique=True)
		
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def get_absolute_url(self):
		return reverse('properties:categories', args=[self.slug])

	def __str__(self):
		return self.name

	def _get_unique_slug(self):
		slug = slugify(self.name)
		unique_slug = slug
		num = 1
		while Category.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self,*args,**kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save()
		

class PropertyManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PropertyManager, self).filter(draft=False)


class Property(models.Model):
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
	main_photo = models.ImageField(upload_to='images/properties/%Y/%m/%d', default='images/properties/property.jpg')
	sub_photo_1 = models.ImageField(upload_to='images/properties/%Y/%m/%d', default='images/properties/property.jpg', blank=True)
	sub_photo_2 = models.ImageField(upload_to='images/properties/%Y/%m/%d', default='images/properties/property.jpg', blank=True)
	sub_photo_3 = models.ImageField(upload_to='images/properties/%Y/%m/%d', default='images/properties/property.jpg', blank=True)
	sub_photo_4 = models.ImageField(upload_to='images/properties/%Y/%m/%d', default='images/properties/property.jpg', blank=True)
	house_name = models.CharField(max_length=55, default='', blank=True, null=True)
	location = models.CharField(max_length=255, default='', blank=True, null=True)
	owner = models.CharField(max_length=55, default='', blank=True, null=True)
	phone = models.CharField(max_length=18, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	conditions = models.TextField(blank=True, null=True)
	rating = models.IntegerField(default=0, blank=True, null=True)

	price = models.IntegerField(default=0, blank=True, null=True)
	size = models.IntegerField(default=0, blank=True, null=True)
	bedrooms = models.IntegerField(default=1, blank=True, null=True)
	bathrooms = models.IntegerField(default=1, blank=True, null=True)
	balcony = models.IntegerField(default=1, blank=True, null=True)
	year_built = models.IntegerField(default=0, blank=True, null=True)
	available_from = models.DateTimeField(auto_now=False, auto_now_add=False)	
	creation_date = models.DateTimeField(default=now)
	created_by = models.CharField(max_length=20, default='', null=True, blank=True)
	floor_no = models.IntegerField(default=1, blank=True, null=True)
	slug = models.SlugField(unique=True)

	draft = models.BooleanField(default=True)
	is_available = models.BooleanField(default=True)

	telephone = models.BooleanField(default=False)
	wifi = models.BooleanField(default=False)
	parking = models.BooleanField(default=False)
	security = models.BooleanField(default=False)
	generator = models.BooleanField(default=False)
	lift = models.BooleanField(default=False)

	objects = PropertyManager()
	
	class Meta:
		verbose_name = 'Property'
		verbose_name_plural = 'Properties'
			

	def __str__(self):
		return self.house_name

	def get_absolute_url(self):
		return reverse('properties:property', kwargs={"slug": self.slug})

	def _get_unique_slug(self):
		slug = slugify(self.house_name)
		unique_slug = slug
		num = 1
		while Property.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save()


class Rating(models.Model):
	property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True, related_name='rev')
	rating = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return str(self.id)
