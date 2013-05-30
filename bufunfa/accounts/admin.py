# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import AccountType, Account

class AccountTypeAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Account, AccountAdmin)
