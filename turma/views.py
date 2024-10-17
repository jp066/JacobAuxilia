from django.http import HttpResponse
from django.shortcuts import render


def turma_page(request):
    if request.user.profile.role == 'Aluno':
        return render(request, 'listar_atividades_turmas.html')
    else:
        return HttpResponse('Acesso negado')