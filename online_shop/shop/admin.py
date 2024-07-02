from django.contrib import admin

# Register your models here.
from shop.models import Category, Product, Comment, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'rating')
    list_filter = ('name', 'price', 'quantity')
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'id')
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_accessible', 'product', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email', 'is_accessible', 'product')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'quantity', 'product', 'time')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email', 'product', 'time')