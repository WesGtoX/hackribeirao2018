from django import forms
from .models import questoes, provas
from django.forms import ModelChoiceField, Select

#Create your forms here

#formulaŕio para cadastro de questões
class questoesForm(forms.ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Descrição',
            'rows': '3',
        }
    ))

    codigo = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Código',
            #'readonly':'readonly',
        }
    ))

    disciplina = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Disciplina',
        }
    ))

    imagem = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={
            'class': 'custom-file-input',
            'placeholder': 'Procurar',
        }
    ))

    class Meta:
        model = questoes
        fields = [
            'descricao',
            'codigo',
            'disciplina',
            'imagem',
        ]

class provaForm(forms.ModelForm):
    questoes = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id':'summernote',
        }
    ))

    class Meta:
        model = provas
        fields = [
            'questoes',
        ]