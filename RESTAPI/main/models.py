from django.db import models
from django.db.models.fields import CharField, IntegerField

class item(models.Model):
    name = CharField(max_length=100)
    category = CharField(max_length= 100, null=True, blank=True)
    price = IntegerField()
    quantity = IntegerField()
    class Meta:
        verbose_name = 'item'
    def __str__(self):
        return self.name

class user(models.Model):
    name = CharField(max_length=50)
    phone = CharField(max_length=25)
    password = CharField(max_length=50)
    def __str__(self):
        return self.name



# Create your models here.
