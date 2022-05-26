from django.shortcuts import render
#from rest_framework import mixins
from core.models import *
from rest_framework import generics
from core.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions

# Create your views here.
# class ListCategory(generics.ListAPIView, mixins.ListModelMixin):
#     serializer_class = CategorySerializer
#     categories = Category.objects.all()


# Class-based view to list elements of a model
class CategoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    """use queryset to map the models"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Class-based view to Retrieve, Update and Destroy elements of a model
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ProductList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer