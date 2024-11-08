from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('traducao', views.traducao, name='traducao'),  # essa view é chamada quando o usuário clica no botão de traduzir. o id serve para identificar o texto que será traduzido
    path('visão-inclusiva', views.visao_inclusiva, name='visao_inclusiva'),
    path('pesquisar-videos', views.pesquisar_videos, name='pesquisar_videos'),
]