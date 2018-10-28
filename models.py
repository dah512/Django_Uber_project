from django.db import models
from django.db import forms
from django.utils import timezone


    
now= timezone.now()  
phonenumber = PhoneNumberField(blank=True)

class Driver(models.Model):
    from phonenumber_field.modelfields import PhoneNumberField
    def__init__(self, phonenumber, smsnumber, rating, picture_url, d_name):
           self.phonenumber = models.PhoneNumberField(blank=True)
           self.smsnumber = models.PhoneNumberField(blank=True)
           self.rating = models.RatingField(forms.ChoiceField)
           self.picture_url = models.URLfield()
           self.d_name =  models.CharField(max_length=20)
      
class Vehicle(models.Model):     
    """Model and Make of Vehicle""" 
    def__init__(self, make, model, license_plate, picture_url):
           self.make = models.CharField(max_length= 20)
           self.model = models.CharField(max_length= 20)
           self.license_plate = models.CharField(max_length= 20)
           self.picture_url = models.URLField()
   
class LocationForm(forms.ModelForm):
    class Meta:
        model = models.Location
        exclude = ('latitude','longitude')
    
class registerForm(forms.ModelForm): 
class Meta:
    model=register
    fields = ('Availability', 'Status')

    def save(self,ip_address, *args, **kwargs):
    g = GeoIP()
    lat, lon = g.lat_lon(ip_address)
    user_location = super(registerForm, self).save(commit=False)
    user_location.latitude = lat
    user_location.longitude = lon
    user_location.save(*args, **kwargs)
 
class Location(models.Model):
from django.contrib.gis.utils import GeoIP       
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=10, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    
    
class Pickup(models.Model):
    def__init__(self, alias, address, latitude, longitude, eta):
           self.alias = models.CharField(max_length=50)
           self.address = models.CharField(max_length= 50)
           self.latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
           self.longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
           self.eta = models.DateTimeField(timezone.now())
    
class Destination(models.Model):
    def__init__(self, alias, address, latitude, longitude, eta):
           self.alias = models.CharField(max_length= 50)
           self.address = models.CharField(max_length= 50)
           self.latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
           self.longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
           self.eta = models.DateTimeField(timezone.now())
    
class Dropoff(models.Model):
    def__init__(self, alias, address, latitude, longitude, eot): 
           self.rider_id= model.CharField(max_length= 50)
           self.address = models.CharField(max_length= 50)
           self.latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
           self.longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
           self.eot= models.BooleanField(default= True)
           self.eot_time= models.DateTimeField(default= now)
           self.eot_text= models.CharField( "Trip ended at:", eot_time) #End of Trip
    

class Rider(models.Model):
    def__init__(self, name, rider_is_member):
           self.name= models.ForiegnKey(Rider, on_delete = models.CASCADE) 
           self.rider_is_member= models.BooleanField(default= true, on_delete = models.CASCADE)
