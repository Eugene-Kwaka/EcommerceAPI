from django.shortcuts import render
from core.models import *
from rest_framework import generics
from core.serializers import *
from rest_framework import permissions
from rest_framework.response import Response
import uuid
from rest_framework import status


# REGISTRATION VIEW
class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
# Post method to create the User
    def post(self, request):
        # serialize the data instance used for validating and deserializing input and serializing output
        serializer = self.get_serializer(data = request.data)
        # check if serializer is valid then save and return responses
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message" : "User Created Successfully",
                "User": serializer.data, 
            },
            # status to show the serializer object has been created
            status=status.HTTP_201_CREATED
            )
        # Else return an error of Bad Request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
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