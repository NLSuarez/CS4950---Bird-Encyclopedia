# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response
from .models import Bird

class BirdList(ListView):
    model = Bird
    template_name = ''
    queryset = ''#Will be changed once models are ironed out

    def get_queryset(self):
        return self.queryset

class BirdEntry(DetailView):
    model = Bird
    template_name = ''

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
