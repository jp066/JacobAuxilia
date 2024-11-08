from django.urls import path
from . import views

urlpatterns = [
    path('traducao/', views.traducao, name='traducao'),
]