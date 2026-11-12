from django.contrib import admin
from .models import Product, Order, OrderItem


# Order Items inside Order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'customer_name',
        'email',
        'phone',
        'total_amount',
        'status',
        'created_at'
    )

    list_filter = ('status', 'created_at')

    search_fields = (
        'customer_name',
        'email',
        'phone'
    )

    inlines = [OrderItemInline]


# Product Admin
admin.site.register(Product)