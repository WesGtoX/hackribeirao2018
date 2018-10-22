from django.db import models

# Create your models here.

class cidade(models.Model):
    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=100)
    data_insercao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'cidade'


class escolas(models.Model):
    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=100)
    quantidade_alunos = models.IntegerField()
    renda = models.CharField(max_length=100)
    ocorrencias = models.CharField(max_length=100)
    quantidade_professores = models.IntegerField()

    data_insercao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'escolas'
