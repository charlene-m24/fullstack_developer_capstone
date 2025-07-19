# Uncomment the following imports before adding the Model code

from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timezone import now

# from .models import CarMake, CarModel

# Registering models with their respective admins
# admin.site.register(CarMake)
# admin.site.register(CarModel)


# Create your models here.


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)

    dealer_id = models.IntegerField()
    name = models.CharField(max_length=255)
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "WAGON"
    TYPE_CHOICES = (
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
    )
    model_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.DateField()

    def __str__(self):
        return f"{self.make} {self.name} ({self.year})"
