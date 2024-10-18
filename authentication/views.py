from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

def cadastroView(request):
    if request.method == 'GET':
        return render(request, 'signUp.html') # Redireciona para a página de cadastro se o método for GET
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        role = request.POST.get('role') # Pega o valor do botão de rádio selecionado
        # Pega os dados do formulário de cadastro    
        user = User.objects.filter(username=username).first() # Verifica se o usuário já existe no banco de dados

        if user:
            return render(request, 'CadastroErro.html') # Redireciona para a página de erro de cadastro

        user = User.objects.create_user(username=username, password=senha) # Cria o usuário no banco de dados
        user.profile.role = role # Define o papel do usuário
        user.save() # Salva o usuário no banco de dados
        return redirect('login') # Redireciona para a página de login

def loginView(request):
    if request.method == 'GET':
        return render(request, 'signIn.html')
    
    else:
        username = request.POST.get('username') # Pega o nome de usuário do formulário
        senha = request.POST.get('senha') # Pega a senha do formulário
        
        user = authenticate(username=username, password=senha) # Autentica o usuário.
        
        if user:
            auth_login(request, user) # Loga o usuário
            if user.profile.role == 'Professor':
                return render(request, 'index_professor.html', {'nome_professor': username}) # Redireciona para a página do professor
            else:
                return render(request, 'index_turma.html') # Redireciona para a página do aluno
        else:
            return render(request, 'loginErro.html', {'error': 'Usuário ou senha inválidos'})


def logout_view(request):
    logout(request)
    return render(request, 'signIn.html')