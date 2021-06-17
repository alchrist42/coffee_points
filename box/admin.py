from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'volume', 'point', 'done', 'created',)
    list_filter = ('point',)
    date_hierarchy = 'created'

admin.site.register(CoffeeType)
admin.site.register(CoffeePoint)
admin.site.register(Order, OrderAdmin)
