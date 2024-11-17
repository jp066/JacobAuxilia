from django.shortcuts import render
from gtts import gTTS
import os
from django.conf import settings
import logging
from .forms import ImagemForm
from .models import Imagem
from pytesseract import pytesseract # Importa o módulo pytesseract de dentro do pacote pytesseract
from PIL import Image


def traducao(request):
    return render(request, 'traducao.html')


def formulario_ler_texto(request):
    return render(request, 'ler_texto.html')


logging.basicConfig(level=logging.DEBUG)

def ler_texto(request):
    if request.method == "POST":
        texto = request.POST.get('texto', '')
        if texto:
            # Garante que o diretório media exista
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)
            # Gera o arquivo de áudio
            audio_path = os.path.join(settings.MEDIA_ROOT, 'output.mp3')
            tts = gTTS(text=texto, lang='pt')
            tts.save(audio_path)
            logging.debug(f"Arquivo de áudio salvo em: {audio_path}")
            # Retorna o template com o áudio embutido
            return render(request, 'ler_texto.html', {'audio_url': f"{settings.MEDIA_URL}output.mp3"})
    return render(request, 'ler_texto.html')


def upload_imagem(request):
    if request.method == "POST":
        form = ImagemForm(request.POST, request.FILES) 
        if form.is_valid():
            imagem = form.save()
            caminho_imagem = imagem.imagem.path 
            
            # Extrair texto
            texto = pytesseract.image_to_string(Image.open(caminho_imagem)) # Extrai o texto da imagem
            imagem.extraido = texto # Salva o texto extraído no objeto
            imagem.save() # Salva o objeto no banco de dados

            # Gera o arquivo de áudio diretamente
            if texto:
                if not os.path.exists(settings.MEDIA_ROOT):
                    os.makedirs(settings.MEDIA_ROOT)
                audio_path = os.path.join(settings.MEDIA_ROOT, 'output.mp3')
                tts = gTTS(text=texto, lang='pt')
                tts.save(audio_path)

                # Redireciona para o template de leitura de texto com o áudio
                return render(request, 'ler_texto.html', {
                    'audio_url': f"{settings.MEDIA_URL}output.mp3",
                    'texto_extraido': texto
                })
    else:
        form = ImagemForm()

    return render(request, "upload.html", {"form": form})