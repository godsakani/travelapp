from django.contrib import admin

from .models import BusModel, CustomerModel, OrderModel
class BusModelAdmin(admin.ModelAdmin):
    list_display = ('name','price')
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('userid','phoneno')
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('username','phoneno','address','ordereditems','status')

admin.site.register(BusModel,BusModelAdmin)
admin.site.register(CustomerModel,CustomerModelAdmin)
admin.site.register(OrderModel,OrderModelAdmin)