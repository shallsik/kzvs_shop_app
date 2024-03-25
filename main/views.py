from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'КЗВС - Главная',
        'content': 'Магазин зоотоваров КЗВС',
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'КЗВС - О нас',
        'content': 'О нас',
    }
    
    return render(request, 'main/about.html', context)