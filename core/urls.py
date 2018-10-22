from django.urls import path
from .views import index, busca, cidade, corrigir_prova

urlpatterns = [
    path('', index, name='index'),
    path('busca/', busca, name='busca'),
    path('cidade/', cidade, name='cidade'),
    path('corrigir_prova/', corrigir_prova, name='corrigir_prova'),
]