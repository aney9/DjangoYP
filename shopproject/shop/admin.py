from django.contrib import admin
from .models import *


# Register your models here.

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass
#
# @admin.register(Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Clothes)
# class ClothesAdmin(admin.ModelAdmin):
#     pass

@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass



@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(CatalogProduct)
class CatalogProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    pass


# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderrAdmin(admin.ModelAdmin):
    pass


