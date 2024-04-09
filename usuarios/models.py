from django.db import models
from cpf_field.models import CPFField

#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#from django.contrib.auth.models import User


class Usuarios(models.Model):
    nome_aluno = models.CharField(max_length=150, null=True, blank=False)
    cpf = CPFField(primary_key=True)
    password = models.CharField(max_length=128, null=True, blank=False)
    escola = models.CharField(max_length=100, null=True, blank=False)
    turma = models.CharField(max_length=7, null=True, blank=False)
    
def __str__(self):
    return f'Nome_aluno: {self.nome_aluno} | {self.cpf} | {self.escola} | {self.turma}'

class MyModel(models.Model):
    # ....
    cpf = CPFField('cpf')