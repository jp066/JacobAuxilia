from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm, VideoSearchForm
from .models import Video


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
    return render(request, 'about_us.html')


@login_required
def visao_inclusiva(request):
    videos = [
        "https://www.youtube.com/watch?v=T3s8oiVK600",
        "https://www.youtube.com/watch?v=2zTLFCfdgME",
        "https://www.youtube.com/watch?v=nasXJb_xsnc",
        "https://www.youtube.com/watch?v=-ZDkdbPqUZg",
        "https://www.youtube.com/watch?v=jH3pbDRx2Xc",
        "https://www.youtube.com/watch?v=vJcQJuH3-so",
        "https://www.youtube.com/watch?v=TeIQtCWV5P8",
        "https://www.youtube.com/watch?v=BAPFjNGtOV8",
        "https://www.youtube.com/watch?v=pu5UD7tYHos"
    ]
    return render(request, 'visao_inclusiva.html', {'videos': videos})


import logging

logger = logging.getLogger(__name__)

@login_required
def pesquisar_videos(request):
    form = VideoSearchForm(request.GET or None)
    videos = Video.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        logger.debug(f"Query: {query}")
        if query:
            videos = videos.filter(titulo__icontains=query)
            logger.debug(f"Filtered videos: {videos}")

    logger.debug(f"Videos: {videos}")

    return render(request, 'visao_inclusiva.html', {
        'videos': videos,
        'form': form,
        'query': form.cleaned_data.get('query', '')
    })



@login_required
def helpme(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES, user=request.user)  # Passa o usuário para o formulário
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para uma página de sucesso após salvar o feedback
    else:
        form = FeedbackForm(user=request.user)  # Passa o usuário para o formulário
        
    return render(request, 'helpme.html', {'form': form})