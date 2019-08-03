# Register your models here.
from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):

     #To diplay in the tabular form With these attribute as metioned below.
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']

    # This is added to filter the product based on available ,created_at...
    list_filter = ['available', 'created_at', 'updated_at']

    #To be editable in the panel.
    list_editable = ['price', 'stock', 'available']

    #To add  the slug from name itself
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
