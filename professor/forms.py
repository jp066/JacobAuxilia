from django import forms
from .models import Atividades, Classes

class AtividadesForm(forms.ModelForm):
    class Meta:
        model = Atividades
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['serie', 'tamanho', 'data_inicio', 'data_fim']  # Corrigido para 'serie' e 'tamanho'
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }