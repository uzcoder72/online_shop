from django.contrib import admin
from django.urls import path

from shop.views import product_list

urlpatterns = [
    path('', product_list, name='products'),
]
