from django.contrib import admin

# Register your models here.
from producttracker.models import TrackProduct
from producttracker.models import Product
from producttracker.models import StoreInventory

admin.site.register(TrackProduct)
admin.site.register(Product)
admin.site.register(StoreInventory)
