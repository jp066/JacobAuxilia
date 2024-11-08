from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homeView(request):
    return render(request, 'home.html')

@login_required
def traducao(request):
    return render(request, 'traducao.html')

@login_required
def dificuldade(request):
    return render(request, 'dificuldade.html')

@login_required
def central_de_ajuda(request):
    return render(request, 'central_de_ajuda.html')

@login_required
def perguntas(request):
    return render(request, 'perguntas.html')

@login_required
def sobre(request):
    return render(request, 'sobre.html')

@login_required
def visao_inclusiva(request):
    videos = range(1, 11)
    return render(request, 'visao_inclusiva.html', {'videos': videos})

@login_required
def pesquisar_videos(request):
    query = request.GET.get('query', '')
    videos = range(1, 11)
    if query:
        videos = [video for video in videos if query.lower() in f'video {video}'.lower()]
    return render(request, 'visao_inclusiva.html', {'videos': videos, 'query': query})