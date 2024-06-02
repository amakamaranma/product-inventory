from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        field = ['id', 'name', 'description', 'supply_price', 'selling_price', 'stock', 'expiry_date', 'category', 'supply_date']


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id','name','description','supply_price','selling_price','stock','expiry_date','category','supply_date']
