from django.contrib import admin
from store.models import Product, ProductImage, ProductType


admin.site.register((Product, ProductType, ProductImage, ))
