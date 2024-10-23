from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastroView, name='cadastro'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logout_view, name='logout'),
    ]