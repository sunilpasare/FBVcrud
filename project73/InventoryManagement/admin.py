from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','Date','Provider','Nameofproduct','Price','Quantity','Amount','Stock']

admin.site.register(Product,ProductAdmin)



