from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _

# Create your models here.

#Tabela provas
class provas(models.Model):
    id = models.AutoField(primary_key=True)

    '''
        O campo de questões é uma chave estrangeira,
        que herda os valores do campo descrição da tabela questões.
    '''
    questoes = models.CharField(max_length=9999)

    def __str__(self):
        return self.questoes

    class Meta:
        db_table = 'provas'


#Tabela de questões
'''
A tabela é responsavel por conter as informações das questões.
'''
class questoes(models.Model):
    id = models.AutoField(primary_key=True)

    '''
        O campo código é gerado com base na escolaridade,
        ano escolar do aluno, disciplina e habilidade.

        Exemplo: (EF06LP01)
    '''
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=1000)
    imagem = models.ImageField(upload_to='imagens', null=True)

    '''
        As alternativas são feitas por base de uma lista,
        concatenadas no momento da inserção no banco.
    '''
    alternativas = models.CharField(max_length=10, null=True)

    '''
        As respostas são feitas por base de uma lista,
        concatenadas no momento da busca no banco.
    '''
    gabarito = models.CharField(max_length=1, null=True)
    disciplina = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'questoes'
