from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'amount', 'date_added', 'user')
    list_filter = ('user',)
    search_fields = ('name', 'description')

