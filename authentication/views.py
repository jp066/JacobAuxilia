import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout

def validar_senha(senha):
    # Verifica se a senha tem mais de 6 caracteres
    if len(senha) < 6:
        return False, "A senha deve ter pelo menos 6 caracteres."

    # Verifica se a senha contém pelo menos uma letra e um número
    if not re.search(r'[A-Za-z]', senha) or not re.search(r'\d', senha):
        return False, "A senha deve conter pelo menos uma letra e um número."

    # Verifica se a senha contém pelo menos um caractere especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False, "A senha deve conter pelo menos um caractere especial."

    return True, ""


def cadastroView(request):
    if request.method == 'GET': 
        return render(request, 'signUp.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'cadastroErro.html') # Usuário já existe

        # Valida a senha
        senha_valida, erro = validar_senha(senha)
        if not senha_valida:
            return render(request, 'senhaFraca.html', {'authentication': {'erro': erro}})

        user = User.objects.create_user(username=username,email=email, password=senha)
        user.save()
        return redirect('login')


def loginView(request):
    if request.method == 'GET':
        return render(request, 'signIn.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'loginErro.html', {'error': 'Usuário ou senha inválidos'})


def logout_view(request):
    logout(request)
    return render(request, 'signIn.html')
