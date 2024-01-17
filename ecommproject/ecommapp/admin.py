from django.contrib import admin
from .models import Product, Order, Cart

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "userid",
        "product_id",
        "product_name",
        "category",
        "desc",
        "price",
        "image",
    ]


class CartAdmin(admin.ModelAdmin):
    list_display = ["userid", "product_id", "qty"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["userid", "product_id", "orderid", "qty"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
