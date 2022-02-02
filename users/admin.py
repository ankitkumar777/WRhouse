from django.contrib import admin

# Register your models here.
from users.models import *

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')
    ordering = ('user',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')
    ordering = ('user',)

