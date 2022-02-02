from django.contrib import admin

# Register your models here.
from warehouse.models import *

admin.site.site_title = "Warehouse Management System"
admin.site.site_header = "Warehouse Management System Admin panel"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'brand')
    ordering = ('name',)
    search_fields = ('name', 'location')
    list_filter = ('name', 'location')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'customer','status',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_status', 'delievered_to')


@admin.register(StockRequest)
class StockRequestAdmin(admin.ModelAdmin):
    list_display = ('product', 'stock_qty', 'supplier')
