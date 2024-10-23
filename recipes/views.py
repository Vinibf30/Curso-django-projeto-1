from django.shortcuts import render
from django.http import HttpResponse


def my_reponse(request):
    return render(request, 'recipes/pages/home.html')


def contato(request):
    return HttpResponse('Conatato')


def sobre(request):
    return HttpResponse('Sobre')
