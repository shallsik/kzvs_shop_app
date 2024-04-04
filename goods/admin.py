from django.contrib import admin

from goods.models import Categories, Products, Brands
    

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    list_display = [ 'name', 'brand', 'quantity', 'price',]
    search_fields = ['name', 'brand', 'description']
    list_filter = [ 'brand', 'category', 'quantity',]

