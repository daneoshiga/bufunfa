# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Purchase, PurchaseAdmin)
