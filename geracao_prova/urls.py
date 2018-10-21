from django.urls import path
from .views import IndexPage, questao, prova, sobre
from django.views.generic.base import TemplateView


urlpatterns = [
    #url index
    path('index/', IndexPage.as_view(template_name='index/index.html'), name='index'),

    #url questão
    path('questao/', questao, name='questao'),

    #url prova
    path('prova/', prova, name='prova'),

    #url sobre
    path('sobre/', sobre, name='sobre'),

]