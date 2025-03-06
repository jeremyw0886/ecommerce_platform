from django.contrib import admin

from .models import Category, Order, OrderItem, Product, UserProfile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # Removed prepopulated_fields since Category doesn't have a slug field


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'available', 'stock')
    list_filter = ('available', 'category')
    search_fields = ('name', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'paid', 'created')
    list_filter = ('paid', 'created')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'state', 'zip_code')
