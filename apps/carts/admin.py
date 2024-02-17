from django.contrib import admin
from .models import Cart

# Register your models here.

@admin.register(Cart)
class CartModel(admin.ModelAdmin):
    fields = ['user', 'product', 'quantity']
    list_filter = []
    list_display = fields
    search_fields = ['user', 'product']
