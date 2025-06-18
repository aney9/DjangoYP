from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, mixins
from shop.models import *
from .permission import *

# class BrandViewSet(viewsets.ModelViewSet):
#     permission_classes = [CustomPermission]
#     serializer_class = BrandSerializer
#     pagination_class = PaginationPage
#
#     def get_queryset(self):
#         queryset = Brand.objects.all()
#         BrandName = self.request.query_params.get('BrandName', None)
#         if BrandName is not None:
#             queryset = queryset.filter(BrandName__icontains=BrandName)
#         return queryset



class BrandViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
     queryset = Brand.objects.all()
     serializer_class = BrandSerializer

class PetTypeSet(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = PetTypeSerializer
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = PetType.objects.all()
        TypeName = self.request.query_params.get('PetType', None)
        if TypeName is not None:
            queryset = queryset.filter(TypeName__icontains=TypeName)
        return queryset

class CategoryProductSet(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = CategoryProductSerializer
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = CategoryProduct.objects.all()
        CategoryName = self.request.query_params.get('CategoryName', None)
        if CategoryName is not None:
            queryset = queryset.filter(CategoryName__icontains=CategoryName)
        return queryset

class CatalogProductSet(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = CatalogProductSerializer
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = CatalogProduct.objects.all()
        ProductName = self.request.query_params.get('ProductName', None)
        if ProductName is not None:
            queryset = queryset.filter(ProductName__icontains=ProductName)
        return queryset

class PromotionSet(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = PromotionSerializer
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Promotion.objects.all()
        PromotionName = self.request.query_params.get('PromotionName', None)
        if PromotionName is not None:
            queryset = queryset.filter(PromotionName__icontains=PromotionName)
        return queryset


class ReviewSet(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = ReviewSerializer
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Review.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id__icontains=id)
        return queryset


class FavoriteSet(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = FavoriteSerializer
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Favorite.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id__icontains=id)
        return queryset


class OrderSet(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = OrderSerializer
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Order.objects.all()
        buyer_surname = self.request.query_params.get('buyer_surname', None)
        buyer_name = self.request.query_params.get('buyer_name', None)
        if buyer_surname is not None:
            queryset = queryset.filter(buyer_surname__icontains=id)
        elif buyer_name is not None:
            queryset = queryset.filter(buyer_name__icontains=id)
        return queryset

class Pos_orderSet(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = Pos_orderSerializer
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Pos_order.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id__icontains=id)
        return queryset
