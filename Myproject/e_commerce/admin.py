from django.contrib import admin
from .models import Customer, Order

# Register your models here

# Register the models
admin.site.register(Customer)
admin.site.register(Order)