from django.contrib import admin

# Register your models here.
from users.models import User

@admin.register(User)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('email',)


