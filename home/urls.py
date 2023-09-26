from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("search", views.search, name="search"),
    path("kart", views.cart, name="cart"),
    path("kart/add/<int:file_id>", views.add_to_cart, name="add_to_cart"),
    path("kart/remove/<int:book_id>", views.remove_book_from_cart, name="remove_book_from_cart"),
    
]
