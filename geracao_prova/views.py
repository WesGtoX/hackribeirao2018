from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import questoes, provas
from .forms import questoesForm, provaForm

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


# Create your views here.

'''
user = User.objects.all()
print(user)
'''
'''
    Sistema CBV
'''

#CBV Index
class IndexPage(TemplateView):
    template_name = 'index/index.html'


#função das questões
def questao(request):
    q = questoes.objects.all()  # Busca pela tabela

    questForm = questoesForm(request.POST or None)

    if request.method == 'POST':
        if questForm.is_valid():
            print(questForm.cleaned_data['codigo'])
            print(questForm.cleaned_data['descricao'])
            print(questForm.cleaned_data['disciplina'])

            questForm.save()
            return redirect('questao')
    print(q)
    
    return render(request, 'questao/questoes.html', {'questForm': questForm})


def prova(request):
    p = provas.objects.all()

    pForm = provaForm(request.POST or None)

    if request.method == 'POST':
        if pForm.is_valid():
            print(pForm.cleaned_data['questoes'])

            pForm.save()
            return redirect('questao')
    print(p)
    
    return render(request, 'prova/provas.html', {'pForm': pForm})


def sobre(request):
    return render(request, 'sobre/sobre.html')