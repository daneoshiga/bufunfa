# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Place

class PlaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)
