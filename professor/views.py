from django.http import HttpResponse
from django.shortcuts import render


def professor_page(request):
    if request.user.profile.role == 'Professor':
        return render(request, 'index_professor.html')
    else:
        return HttpResponse('Acesso negado')