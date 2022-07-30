from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from more_itertools import first
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Location(models.Model):
    group = models.CharField(verbose_name='Group', max_length=32)
    district = models.CharField(verbose_name='District', max_length=32)
    region = models.CharField(verbose_name='Region', max_length=32)
    # staff = models.OneToOneField(User, on_delete='')
    
    def __str__(self) -> str:
        return self.district
    
    
class Participant(models.Model):    
    first_name = models.CharField(verbose_name='First name' ,max_length=32)
    last_name = models.CharField(verbose_name='Last name' ,max_length=32)
    gender = models.CharField(verbose_name='Gender',max_length=10)
    age = models.CharField(verbose_name='Age', null=True, max_length=10) 
    phone_no = PhoneNumberField(unique = True, null=False, blank = False)
    email = models.EmailField(verbose_name='Email' ,max_length=254)
    linkedin = models.CharField(verbose_name='LinkedIn', null=True, max_length=60) 
    address = models.CharField(verbose_name='Address', null=True ,max_length=100)
    town = models.CharField(verbose_name='Town/City', null=True, max_length=100)
    state  = models.CharField(verbose_name='State', null=True, max_length=100)
    school = models.CharField(verbose_name='School', null=True, max_length=100)
    profession = models.CharField(verbose_name='Profession', null=True, max_length=100)
    member = models.CharField(verbose_name='DLBC Member', max_length=5)
    denomination = models.CharField(verbose_name='Denomination', null=True, max_length=254)
    # program = models.CharField(verbose_name='Program', null=True, max_length=50)
    
    @property
    def full_name(self):
        return  f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.full_name
    
class Convert(models.Model):
    first_name = models.CharField(verbose_name='First name' ,max_length=32)
    last_name = models.CharField(verbose_name='Last name' ,max_length=32)
    gender = models.CharField(verbose_name='Gender',max_length=10)
    age = models.CharField(verbose_name='Age', null=True, max_length=10) 
    phone_no = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField(verbose_name='Email' ,max_length=254)
    address = models.CharField(verbose_name='Address', null=True ,max_length=100)
    town = models.CharField(verbose_name='Town/City', null=True, max_length=100)
    state  = models.CharField(verbose_name='State', null=True, max_length=100)
    school = models.CharField(verbose_name='School', null=True, max_length=100)
    profession = models.CharField(verbose_name='Profession', null=True, max_length=100)
    # program = models.CharField(verbose_name='Program', null=True, max_length=50)
    
    @property
    def full_name(self):
        return  f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.full_name