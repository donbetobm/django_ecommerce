from django.contrib import admin

from .models import Category, Product

# Register your models here.


# Django makes the registration for us
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =  ['name', 'slug']
    # Django know what to do with the filters provided and will set the configuration needed for it
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter  = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug' : ('tittle',)}

