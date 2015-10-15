# -*- coding: utf-8 -*-
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
