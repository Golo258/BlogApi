from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from .models import Category, Product, Brand
from drf_spectacular.utils import extend_schema
from rest_framework import status
from django.shortcuts import get_object_or_404


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
        list_query_set = self.queryset.order_by("pk")
        serializer = BrandSerializer(list_query_set, many=True)
        return Response(serializer.data)

    @extend_schema(request=BrandSerializer, responses=BrandSerializer)
    def create(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=None, responses=BrandSerializer)
    def retrieve(self, request, pk=None):
        brand = get_object_or_404(self.queryset, pk=pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    @extend_schema(request=BrandSerializer, responses=BrandSerializer)
    def update(self, request, pk=None):
        brand = Brand.objects.get(pk=pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=None, responses=None)
    def destroy(self, request, pk=None):
        brand_to_remove = get_object_or_404(self.queryset,pk=pk)
        brand_to_remove.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ProductView(viewsets.ViewSet):
    """
    Product Viewset to view all Product
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
