import random

from django.shortcuts import render
from django.views.generic import  TemplateView


from .models import Category, Item

class Homepage(TemplateView):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        filter = request.GET['filter'] if 'filter' in request.GET else ''
        # print("Filter is ", filter)
        categories = Category.objects.all()
        items = Item.objects.all( ) if not filter else Item.objects.filter(category__category__icontains=filter)
        stars = [('★' * i.stars) +  ('☆' * abs(i.stars - 5 ) ) for i in items  ]
        itemlist = [
            { 'item' : i ,  'star': j} for i,j in zip(items, stars)
        ]
        # print(showcase)
        context = {
            'items' : items, 
            'categories' : categories,
            'stars' : stars,
            'itemlist' : itemlist
        }
        # print(stars)
        
        return render(request, self.template_name, context)