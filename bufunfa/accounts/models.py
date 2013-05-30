# -*- coding: utf-8 -*-
from django.db import models

class AccountType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.ForeignKey('AccountType')
    parent = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.name
