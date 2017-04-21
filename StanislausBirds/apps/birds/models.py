# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Bird(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Species = models.CharField(max_length=100, unique=True)
    Description = models.TextField()
    Image = models.ImageField(blank=True, null=True) #requires pillow (pip install pillow)
    Sound = models.FileField(blank=True, null=True)
    Diet = models.TextField(blank=True, null=True)
    Sleep = models.CharField(max_length=35, blank=True, null=True)
    Habitat = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('Name', )

    def __unicode__(self):
        return u'{}'.format(self.Name)
