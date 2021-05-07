from django.contrib import admin

# Register models here


from .models import Product
admin.site.register(Product)