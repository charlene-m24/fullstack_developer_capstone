from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline



# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)