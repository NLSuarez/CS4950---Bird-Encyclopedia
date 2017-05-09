# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Bird(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    species = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True) #requires pillow (pip install pillow)
    sound = models.FileField(blank=True, null=True)
    diet = models.TextField(blank=True, null=True)
    sleep = models.CharField(max_length=35, blank=True, null=True)
    habitat = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return '%s' % (self.name)
    #def __unicode__(self):
        #return u'{}'.format(self.Name)
