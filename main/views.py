from django.http import HttpResponse
from django.shortcuts import render

from django.conf import settings
from django.shortcuts import redirect

from goods.models import Categories


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


 
 
def error_404_view(request, exception):
   
    return render(request, '404.html')