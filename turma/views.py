from django.shortcuts import render


def turma_page(request):
    return render(request, 'turma.html')