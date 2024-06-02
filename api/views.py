from django.shortcuts import render
from .serializers import CategorySerializer, ProductCreateSerializers, ProductSerializers
from .models import Product, Category
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics


# Create your views here.
class AddCategoryEndpoint(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "pk"


class ProductEndpoint(generics.ListCreateAPIView):
    serializer_class = ProductCreateSerializers
    queryset = Product.objects.all()
    lookup_field = "pk"


# class ProductsListEndpoint(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#     lookup_field = 'pk'
#     permission_classes = [AllowAny]


class CategoryListEndpoint(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
