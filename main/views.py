from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    
    categories = Categories.objects.all()

    context = {
        'title': 'КЗВС - Главная',
        'content': 'Магазин зоотоваров КЗВС',
        'categories': categories,
        
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'КЗВС - О нас',
        'content': 'О нас',
    }
    
    return render(request, 'main/about.html', context)