
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from .models import Category, Product, Brand
from drf_spectacular.utils import extend_schema

class CategoryView(viewsets.ViewSet):
    """
    Category Viewset for viewing product Categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):  # how to return data
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

class BrandView(viewsets.ViewSet):
    """
        Brand Viewset to view all product Brands
    """
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    

class ProductView(viewsets.ViewSet):
    """
        Product Viewset to view all Product
    """
    
    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    