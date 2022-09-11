from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title','slug', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productname', 'seller', 'updated', 'status','category_to_str')
    list_filter = ('status', 'publish', 'created', 'seller')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('productname',), 'description':('body',)}
    raw_id_fields = ('seller',)
    date_hierarchy = 'publish'
    ordering = ('-created',)
    list_editable = ('status',)
    list_display_links = ('productname',)

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = "دسته بندی"
 
