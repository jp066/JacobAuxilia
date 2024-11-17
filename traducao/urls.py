from django.urls import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('traducao/', views.traducao, name='traducao'),
    path('view-text', views.ler_texto, name='ler_texto'),
    path('input-text/', views.formulario_ler_texto, name='formulario'),
    path('upload-image', views.upload_imagem, name='upload-image'),
]