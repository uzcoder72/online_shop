from django.contrib import admin
from django.urls import path
from shop.views import product_detail

from shop.views import home_page, detail_page, about_page
from shop.delete import delete_product

urlpatterns = [
    path('', home_page, name='index'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('category/<slug:category_slug>/products',home_page,name='product_category'),
    path('detail/<int:product_id>/', detail_page, name='detail'),
    path('about/', about_page, name='about'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product')
]
