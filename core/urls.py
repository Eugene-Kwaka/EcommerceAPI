from django.urls import path
from core.views import *

urlpatterns = [
    # Path that will display all the categories
    path('categories', CategoryList.as_view(), name="categories"),
    # Path to display the details of a specific category
    path('categories/<int:pk>/', CategoryDetail.as_view(), name="category"),

    # Path that will display all the books
    path('books', BookList.as_view(), name="books"),
    # Path to display the details of a specific book
    path('books/<int:pk>/', BookDetail.as_view(), name="book"),
    
    # Path that will display all the products
    path('products', ProductList.as_view(), name="products"),
    # Path to display the details of a specific product
    path('products/<int:pk>/', ProductDetail.as_view(), name="product"), 

    # Path that will display users carts
    path('carts', CartList.as_view(), name="carts"),
    # Path to display the details of a specific product
    path('cart/<int:pk>/', CartDetail.as_view(), name="cartdetail"),
]