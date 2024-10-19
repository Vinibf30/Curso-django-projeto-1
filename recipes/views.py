from django.shortcuts import render
from django.http import HttpResponse


def my_reponse(response):
    return HttpResponse('HOME')


def contato(response):
    return HttpResponse('Conatato')


def sobre(response):
    return HttpResponse('Sobre')
