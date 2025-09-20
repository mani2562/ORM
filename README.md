# Ex02 Django ORM Web Application
## Date: 20.09.2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
admin.py

from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('cid', 'cname', 'brand', 'price', 'year')

models.py

from django.db import models

# Create your models here.
from django.db import models

class Car(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.cname

~~~


## OUTPUT

![alt text](<Screenshot 2025-09-20 145533.png>)

## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
