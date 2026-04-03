from django.contrib import admin
from LEOsCafeSiteapp.models import OrderItem
from LEOsCafeSiteapp.models import CoffeeBeanItem

# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('Oname', 'Otemperature', 'Ocupnumber', 'Oodertime')
    search_fields = ('Oname', 'Otemperature')
    list_filter = ('Otemperature',)

admin.site.register(OrderItem,OrderItemAdmin)

class CoffeeBeanItemAdmin(admin.ModelAdmin):
    list_display = ('CBname', 'CBcoffeeshop', 'CBplace', 'CBroasting', 'CBprice', 'CBflavor', 'CBurl', 'CBcoffeetoday')
    search_fields = ('CBname', 'CBcoffeeshop', 'CBplace')
    list_filter = ('CBplace', 'CBroasting')

admin.site.register(CoffeeBeanItem,CoffeeBeanItemAdmin)