from rest_framework import serializers
from core.models import *
from django.contrib.auth.models import User


# # Serializer for the user model 
# class UserSerializer(serializers.ModelSerializer):
#     # User has a relationship with the model instance in which one User can add many books to a Cart
#     books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
#     # User has a relationship with the model instance in which one User can add many products to a Cart    
#     products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'books', 'products']


# REGISTRATION SERIALIZER
class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = [ 'id', 'first_name', 'last_name', 'email', 'username', 'password']

    # Functions to overide some methods
    def validate(self, args):
        # get the user email
        email = args.get('email', None)
        # get the username
        username = args.get('username', None)
        # check if the email exists then give an error if it is already used
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        # check if the username is already taken and if so give a validation error
        if User.objects.filter(username=username).first():
            raise serializers.ValidationError({'username': ('username already exists')})

        # return the validated arguments
        return super().validate(args)


    def create(self, validated_data):
        # validated data in this case is **kwargs
        return User.objects.create_user(**validated_data)


# The User who created a cart
# Associates the cart to the specific user who created the cart
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
    # The book collection in cart will display an array on book items that are read-only and cannot be used during CREATE OR UPDATE
    books = BookSerializer(read_only=True, many=True)
    # The product collection in cart will display an array on product items that are read-only and cannot be used during CREATE OR UPDATE
    products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ['cart_id', 'created_at', 'books', 'products']