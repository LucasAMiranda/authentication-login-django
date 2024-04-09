from django import forms
from .models import Usuarios


class CustomLoginForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['cpf', 'password'] 

        widgets = {
            'password': forms.PasswordInput(),  # Para mascarar a entrada da senha no HTML
        }



class CadastroForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome_aluno', 'cpf', 'password', 'escola', 'turma']

        widgets = {
            'password': forms.PasswordInput(),  # Para mascarar a entrada da senha no HTML
        }