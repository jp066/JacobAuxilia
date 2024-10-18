from django.urls import path
from . import views

urlpatterns = [
    path('turma/', views.turma_page, name='turmas'),
    ]