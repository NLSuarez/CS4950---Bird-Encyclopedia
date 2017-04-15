# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Bird(models.Model):
    Common_Name = models.CharField(max_length=100, unique=True)
    Species_Name = models.CharField(max_length=100, unique=True)
    Short_Description = models.TextField()
    Image_Ref = models.ImageField(blank=True, null=True) #requires pillow (pip install pillow)
    Sound_Ref = models.FileField(blank=True, null=True)
    Diet = models.TextField(blank=True, null=True)
    Sleeping_Habits = models.CharField(max_length=35, blank=True, null=True)
    Habitat = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('Common_Name', )

    def __unicode__(self):
        return u'{}'.format(self.Common_Name)
