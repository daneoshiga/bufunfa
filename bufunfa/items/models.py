# -*- coding: utf-8 -*-
from django.db import models

from model_utils import Choices

class ItemsType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    UNIT = Choices('kg', 'ml', 'un')

    purchase = models.ForeignKey('purchase.Purchase')
    account = models.ForeignKey('accounts.Account', limit_choices_to =
                                {'type__name': 'Despesa'})
    name = models.CharField(max_length=100)
    type = models.ForeignKey('ItemsType')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(choices=UNIT, default=UNIT.un, max_length = 20)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return '%s, %.2f x %.3f %s = %.2f' % (self.name,
                                              self.unit_price, self.quantity,
                                              self.unit, self.total)

