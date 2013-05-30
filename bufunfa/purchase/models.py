# -*- coding: utf-8 -*-
from django.db import models

from model_utils.models import TimeStampedModel

class Purchase(TimeStampedModel):
    '''
    Sum of value from all items of Purchase
    i = Item.objects.filter(purchase_id=1).aggregate(Sum('total'))
    '''
    place = models.ForeignKey('places.Place')
    account = models.ForeignKey('accounts.Account')

    def __unicode__(self):
        return '%s, %s, %s' % (unicode(self.created), self.place, self.account)
