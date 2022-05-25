#from django.shortcuts import render
#from rest_framework import mixins
from core.models import *
from rest_framework import generics
from core.serializers import *
from core.serializers import CategorySerializer

# Create your views here.
# class ListCategory(generics.ListAPIView, mixins.ListModelMixin):
#     serializer_class = CategorySerializer
#     categories = Category.objects.all()


# Class-based view to list elements of a model
class CategoryList(generics.ListCreateAPIView):
    """use queryset to map the models"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Class-based view to Retrieve, Update and Destroy elements of a model
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
