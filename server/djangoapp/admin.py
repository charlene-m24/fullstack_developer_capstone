from django.contrib import admin

from .models import CarMake, CarModel

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)


class CarModelInline(admin.StackedInline):
    model = CarModel


# # CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ["make", "name", "dealer_id", "model_type", "year"]
    search = ["make", "name"]
    filter = ["make", "dealer_id", "model_type", "year"]


# # CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ["name", "description", "color"]
    search = ["name"]
    inlines = [CarModelInline]
