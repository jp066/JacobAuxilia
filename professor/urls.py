from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.professor_page, name='professor'),
    path('atividades/', views.lista_atividades, name='lista-atividades'),
    path('turmas/', views.lista_turmas, name='turma-atividades'),    
    path('criar-atividades/', views.criar_atividade, name='criar-atividades'),
    path('criar-turma/', views.criar_classe, name='criar-classe'),
    path('detalhes-atividades/<int:id>/', views.detalhes_atividade, name='atividades-detalhes'),
    path('detalhes-turma/<int:id>/', views.detalhes_turma, name='turmas-detalhes'),
    path('delete-atividades-page', views.atividade_delete_page, name='atividade-delete-page'),
    path('delete-turma-page', views.turma_delete_page, name='turma-delete-page'),
    path('delete-atividades/<int:id>/', views.atividade_delete, name='atividade-delete'),
    path('delete-turma/<int:id>/', views.turma_delete, name='turma-delete'),
    ]