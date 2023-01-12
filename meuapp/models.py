from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    modalidade = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)