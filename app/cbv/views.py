from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Book

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favourit_publishers'

class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context
