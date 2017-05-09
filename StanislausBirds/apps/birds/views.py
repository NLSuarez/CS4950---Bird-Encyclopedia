# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import render_to_response
from .models import Bird

class BirdList(ListView):
    model = Bird
    template_name = 'birds/birds_list.html'
    queryset = Bird.objects.all()
    paginate_by = 20

    def get_queryset(self):
        return self.queryset

class BirdEntry(DetailView):
    model = Bird
    template_name = 'birds/bird.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
