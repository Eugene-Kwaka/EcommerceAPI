from rest_framework import serializers
from core.models import *


# Serializer for the user model 
class UserSerializer(serializers.ModelSerializer):
    # User has a relationship with these model instance in which one User can add many books to a Cart
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    # User has a relationship with these model instance in which one User can add many products to a Cart    
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'books', 'products']

# The User who created a cart
class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'category', 'author', 'isbn', 'pages', 'price', 'stock', 'description', 'imageUrl', 'status', 'date_created']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_tag', 'name', 'category', 'price', 'stock', 'imageUrl', 'status', 'date_created']


class CartSerializer(serializers.ModelSerializer):
    # This will display the user who created the cart with many=False to show only one User has one cart
    cart_id = CartUserSerializer(read_only=True, many=False)
    # The book in cart will display an array on book items that are read-only and cannot be used during CREATE OR UPDATE
    books = BookSerializer(read_only=True, many=True)
    # The products in cart will display an array on product items that are read-only and cannot be used during CREATE OR UPDATE
    products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ['cart_id', 'created_at', 'books', 'products']