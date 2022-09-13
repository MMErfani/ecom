from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(gateway_check)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'payment_status', 'user')
    list_filter = ('payment_status', 'user')
    search_fields = ('amount', 'user')
