from django.contrib import admin
from .models import Customer, Order, OrderItem, Product, courses, Tutorials, ShippingAddress

# Register your models here.
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['address','city','zipcode']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ("name__startswith",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ("name__startswith",)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ("name__startswith",)


class TutorialsAdmin(admin.ModelAdmin):
    list_display = ['course']
    search_fields = ("name__startswith",)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(courses, CoursesAdmin)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tutorials, TutorialsAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress, ShippingAddressAdmin)

