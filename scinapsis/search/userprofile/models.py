from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.core.validators import RegexValidator

# Create your models here.
class PhoneModel(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True) # validators should be a list


class AddressModel(models.Model):
    street = models.CharField(max_length=100, default="")
    province = models.CharField(max_length=20, default="")
    country = models.CharField(max_length=20, default="")


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    first_name = models.CharField(max_length=50, default="")
    middle_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    phone = models.ForeignKey(PhoneModel, null=True)
    address = models.ForeignKey(AddressModel, null=True)
    email = models.EmailField()
    image = models.ImageField(blank=True, null=True)
    
    
