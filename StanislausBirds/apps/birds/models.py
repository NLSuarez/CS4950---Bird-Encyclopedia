# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
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

    def __str__(self):
        return '%s' % (self.Name)
    #def __unicode__(self):
        #return u'{}'.format(self.Name)
