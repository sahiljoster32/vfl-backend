from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField
from django.core.validators import MaxValueValidator

# Create your models here.

class Vendor(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    products = ListCharField(base_field = models.CharField(max_length=20), size=10, max_length=(21*10)) #20 products at max with commas
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    phone = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    details = models.CharField(max_length=255)

    def __str__(self):
        return self.name