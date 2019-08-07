from django import forms
from .models import Category, Property

class AddPropertyForm(forms.Form):
    # category = forms.ModelChoiceField(Category.objects.all(), required=False, widget=forms.Select())
    main_photo = forms.ImageField(required=True)
    sub_photo_1 = forms.ImageField(required=False)
    sub_photo_2 = forms.ImageField(required=False)
    sub_photo_3 = forms.ImageField(required=False)
    sub_photo_4 = forms.ImageField(required=False)
    house_name = forms.CharField(max_length=55, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control',}))
    location = forms.CharField(max_length=255, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control',}))
    owner = forms.CharField(max_length=55, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control',}))
    phone = forms.CharField(max_length=18, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control',}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control md-textarea',}))
    conditions = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control md-textarea',}))

    price = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    size = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    bedrooms = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    bathrooms = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    balcony = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    year_built = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    available_from = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    created_by = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    floor_no = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    draft = forms.BooleanField(required=False)

    telephone = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input',}))
    wifi = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input',}))
    security = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input',}))
    parking = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input',}))
    generator = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input',}))
    lift = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input',}))

    def clean(self):
        main_photo = self.cleaned_data.get('main_photo')
        sub_photo_1 = self.cleaned_data.get('sub_photo_1')
        sub_photo_2 = self.cleaned_data.get('sub_photo_2')
        sub_photo_3 = self.cleaned_data.get('sub_photo_3')
        sub_photo_4 = self.cleaned_data.get('sub_photo_4')
        house_name = self.cleaned_data.get('house_name')
        location = self.cleaned_data.get('location')
        owner = self.cleaned_data.get('owner')
        phone = self.cleaned_data.get('phone')
        description = self.cleaned_data.get('description')
        conditions = self.cleaned_data.get('conditions')
        price = self.cleaned_data.get('price')
        size = self.cleaned_data.get('size')
        bedrooms = self.cleaned_data.get('bedrooms')
        bathrooms = self.cleaned_data.get('bathrooms')
        balcony = self.cleaned_data.get('balcony')
        year_built = self.cleaned_data.get('year_built')
        available_from = self.cleaned_data.get('available_from')
        floor_no = self.cleaned_data.get('floor_no')
        created_by = self.cleaned_data.get('created_by')

        # rating = self.cleaned_data.get('rating')

    def addProperty(self):
        main_photo = self.cleaned_data.get('main_photo')
        sub_photo_1 = self.cleaned_data.get('sub_photo_1')
        sub_photo_2 = self.cleaned_data.get('sub_photo_2')
        sub_photo_3 = self.cleaned_data.get('sub_photo_3')
        sub_photo_4 = self.cleaned_data.get('sub_photo_4')
        house_name = self.cleaned_data.get('house_name')
        location = self.cleaned_data.get('location')
        owner = self.cleaned_data.get('owner')
        phone = self.cleaned_data.get('phone')
        description = self.cleaned_data.get('description')
        conditions = self.cleaned_data.get('conditions')

        price = self.cleaned_data.get('price')
        size = self.cleaned_data.get('size')
        bedrooms = self.cleaned_data.get('bedrooms')
        bathrooms = self.cleaned_data.get('bathrooms')
        balcony = self.cleaned_data.get('balcony')
        year_built = self.cleaned_data.get('year_built')
        available_from = self.cleaned_data.get('available_from')
        floor_no = self.cleaned_data.get('floor_no')
        created_by = self.cleaned_data.get('created_by')

        telephone = self.cleaned_data.get('telephone')
        wifi = self.cleaned_data.get('wifi')
        parking = self.cleaned_data.get('parking')
        generator = self.cleaned_data.get('generator')
        security = self.cleaned_data.get('security')
        lift = self.cleaned_data.get('lift')

        # rating = self.cleaned_data.get('rating')

        add = Property(main_photo=main_photo, sub_photo_1=sub_photo_1, 
            sub_photo_2=sub_photo_2, sub_photo_3=sub_photo_3, sub_photo_4=sub_photo_4, 
            house_name=house_name, location=location, owner=owner, phone=phone, 
            description=description, conditions=conditions,
            price=price, size=size, bedrooms=bedrooms, 
            bathrooms=bathrooms, balcony=balcony, year_built=year_built, 
            available_from=available_from, created_by=created_by, floor_no=floor_no, 
            telephone=telephone, wifi=wifi, parking=parking, security=security, 
            generator=generator, lift=lift
        )

        return add


class PropertyEditForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ('category', 'creation_date', 'slug', 'draft')
        #fields = '__all__'