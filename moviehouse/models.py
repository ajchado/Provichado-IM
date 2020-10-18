from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length = 100)
    middlename = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    barangay = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    zipcode = models.IntegerField()
    country = models.CharField(max_length = 100)
    birthday = models.DateField(default = 
    datetime.now().strftime('%Y-%m-%d'))
    status = models.CharField(max_length = 100)
    
    class Meta:
        db_table = "Person"

class DvdRegistration(models.Model):
    dateregistered = models.DateField(default = 
    datetime.now().strftime('%Y-%m-%d'))
    sku = models.AutoField(primary_key = True)
    genre = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    reldate = models.DateField(default = 
    datetime.now().strftime('%Y-%m-%d'))
    dfirstname = models.CharField(max_length = 100)
    dlastname = models.CharField(max_length = 100)
    cfirstname = models.CharField(max_length = 100)
    clastname = models.CharField(max_length = 100)
    price = models.IntegerField()
    items = models.IntegerField()
    dvdpic = models.FileField(default='settings.MEDIA_ROOT/hospital.jpg')
    isDeleted = models.BooleanField(default = False)  

    class Meta:
        db_table = "DvdRegistration"

class CustomerRegistration(Person):
    profilepic = models.FileField(default='settings.MEDIA_ROOT/seulgo.png')  
    registereddate = models.DateField(default = 
    datetime.now().strftime('%Y-%m-%d'))
    employeeid = models.AutoField(primary_key = True)
    slastname = models.CharField(max_length = 100)
    sfirstname = models.CharField(max_length = 100)
    slastname = models.CharField(max_length = 100)
    soccupation = models.CharField(max_length = 100)
    children = models.IntegerField()
    order = models.ManyToManyField(DvdRegistration)

    class Meta:
        db_table = "CustomerRegistration"