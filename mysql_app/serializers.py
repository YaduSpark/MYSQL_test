from rest_framework import serializers

from mysql_app.models import ProductCategory, ProductManufacturer, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductManufacturer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=ProductCategory.objects.all(),
        slug_field='name'
    )

    manufacturer = serializers.SlugRelatedField(
        queryset = ProductManufacturer.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'manufacturer']