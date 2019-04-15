import graphene
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from graphene_django import DjangoObjectType

from store.models import Product, ProductImage


class ImageType(DjangoObjectType):

    sized_image = graphene.String(size=graphene.String())

    class Meta:
        model = ProductImage

    def resolve_sized_image(self, info, **kwargs):
        size = kwargs.get('size')
        return self.image.thumbnail[size]


class Products(DjangoObjectType):

    images = graphene.List(ImageType)

    class Meta:
        model = Product

    def resolve_images(self, info):

        return self.product_images.all()


class Query(graphene.ObjectType):

    products = graphene.List(Products, image_size=graphene.String())
    product = graphene.Field(Products, id=graphene.Int())

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_product(self, info, **kwargs):
        _product = None
        _id = kwargs.get('id')
        if _id:
            try:
                _product = Product.objects.get(pk=_id)
            except (ObjectDoesNotExist, MultipleObjectsReturned):
                print('(ObjectDoesNotExist, MultipleObjectsReturned)')
            except Exception as e:
                print(f'{e}')
        return _product


schema = graphene.Schema(query=Query)
