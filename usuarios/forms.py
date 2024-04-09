from django import forms
from .models import Usuarios


class CustomLoginForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['cpf', 'password'] 



class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome_aluno', 'cpf', 'password', 'escola', 'turma']