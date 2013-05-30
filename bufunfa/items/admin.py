# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import ItemsType, Item

class ItemsTypeAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(ItemsType, ItemsTypeAdmin)
admin.site.register(Item, ItemAdmin)
