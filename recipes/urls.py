from django.urls import path
from recipes.views import contato, sobre, my_reponse

urlpatterns = [
    path('contato/', contato),
    path('HOME/', my_reponse),
    path('sobre/', sobre),
    path('', my_reponse)
]
