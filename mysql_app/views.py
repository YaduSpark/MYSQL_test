from rest_framework import generics

from mysql_app.serializers import CategorySerializer, ManufacturerSerializer, ProductSerializer
from mysql_app.models import ProductCategory, ProductManufacturer, Product
# Create your views here.


class CategoryListView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer


class ManufacturerListView(generics.ListCreateAPIView):
    queryset = ProductManufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ManufacturerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductManufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer