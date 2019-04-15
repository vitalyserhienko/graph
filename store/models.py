from django.db import models
from versatileimagefield.fields import VersatileImageField


class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_images')
    image = VersatileImageField(upload_to='product/images/')

    def __str__(self):
        return f'image_{self.id}_{self.product.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    # image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
