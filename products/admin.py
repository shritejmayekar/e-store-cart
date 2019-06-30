from django.contrib import admin
from products.models import Product,Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    prepopulated_fields= {'slug':('name',)}
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

