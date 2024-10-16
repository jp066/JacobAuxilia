from django.shortcuts import render

def cadastro(request):
    return render(request, 'signUp.html')

def login(request):
    return render(request, 'signIn.html')