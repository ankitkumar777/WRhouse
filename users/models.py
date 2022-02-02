from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,limit_choices_to={'groups__name': "supplier"})
    email =models.EmailField(max_length=254, null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user.username)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,limit_choices_to={'groups__name': "customer"})
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user.username)

