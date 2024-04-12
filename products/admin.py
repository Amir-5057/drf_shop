from django.contrib import admin

from products.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount',
                    'created_at', 'category',
                    'view_count']


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['title', 'product']


@admin.register(CharacteristicValue)
class CharacteristicValueAdmin(admin.ModelAdmin):
    list_display = ['title', 'characteristic']


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'status', 'total_price', 'created_at']
    list_filter = ['status']
    inlines = [OrderItemInline]
