from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'КЗВС',
        'content': 'Главная страница магазина - КЗВС',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False,
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')