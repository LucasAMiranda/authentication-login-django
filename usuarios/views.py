from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.urls import  reverse
from django.contrib import messages
from .forms import CustomLoginForm, CadastroForm

#from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuarios
from .serializers import UserSerializer


@api_view(['GET'])
def get_users(request):
    
    if request.method == 'GET':
        
        users = Usuarios.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

#https://www.youtube.com/watch?v=Q2tEqNfgIXM&t=596s    >>>> 25:37
# criar o get do id


@api_view(['GET'])
def get_by_cpf(request, cpf):
    
    try:
        user = Usuarios.objects.get(pk=cpf)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)



@api_view(['POST']) 
def login(request):
    if request.method == "POST":
        try:
            cpf = request.POST.get('cpf')
            senha = request.POST.get('senha')
            user = authenticate(request, cpf=cpf, password=senha)
            if user is not None:
                # O usuário foi autenticado com sucesso, então você pode prosseguir
                serializer = UserSerializer(user)  
                return Response(serializer.data)
            else:
                # As credenciais do usuário estão incorretas, então retorne uma resposta de erro
                return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_400_BAD_REQUEST)
        except Usuarios.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)


def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            # Verifica se já existe um usuário com este CPF
            if Usuarios.objects.filter(cpf=cpf).exists():
                messages.error(request, "Este CPF já está registrado.")
            else:
                form.save()
                messages.success(request, "Cadastro realizado com sucesso!")
                return redirect('login') # Redireciona para a página inicial após o login
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            password = form.cleaned_data['password']
            user = authenticate(request, cpf=cpf, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login efetuado com sucesso!")
            else:
                # Caso as credenciais sejam inválidas, exibir uma mensagem de erro
                messages.error(request, "Credenciais inválidas. Tente novamente.")
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})