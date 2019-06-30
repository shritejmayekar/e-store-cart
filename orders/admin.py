from django.contrib import admin
from orders.models import Order,OrderItem

# Register your models here.
class OrderInLineItem(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','postal_code','city','address','created_at','updated_at']
    inlines = [OrderInLineItem]
admin.site.register(Order,OrderAdmin)