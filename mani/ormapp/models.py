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
