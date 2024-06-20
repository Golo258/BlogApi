from rest_framework import serializers
from .models import Product, Category, Brand


class CategorySerializer(serializers.ModelSerializer):

    class Meta:  # what fields will the serializer have
        model = Category
        fields = ['id', 'name']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = "__all__"
