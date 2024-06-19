from django.contrib import admin
from .models import Product, Catagory, Customar , Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Catagory)
admin.site.register(Customar)
admin.site.register(Order)
