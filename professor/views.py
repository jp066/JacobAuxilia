from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from professor.models import Atividades, Classes
from django.urls import reverse
from django.http import HttpResponseRedirect
from professor.forms import AtividadesForm, ClassForm
from django.contrib import messages


@login_required
def professor_page(request):
    username = request.user.username
    atividades = Classes.objects.all()  # Obtém todas as atividades ou turmas do banco de dados
    turmas = Classes.objects.all()  # Obtém todas as turmas do banco de dados
    # Combine todos os dados em um único dicionário
    context = {
        'nome_professor': username,
        'atividades': atividades,
        'turmas': turmas
    }
    return render(request, 'index_professor.html', context)


@login_required
def turma_page(request):
    return render(request, 'index_turma.html')


@login_required
def lista_atividades(request):
    atividades = Atividades.objects.all()  # Busca todas as atividades no banco de dados
    return render(request, 'lista_atividades.html', {'atividades': atividades})


@login_required
def lista_turmas(request):
    classes = Classes.objects.all()
    context = {
        'turmas': classes # turmas é o nome da variável que será usada no template
        }
    return render(request, 'index_turma_professor.html', context=context)


def criar_atividade(request):
    if request.method == 'POST':
        form = AtividadesForm(request.POST) # o request.POST é para pegar os dados do formulário
        if form.is_valid():
            form = form.save(commit=False) # o commit=False é para não salvar no banco de dados ainda
            form.save() # Salva o objeto no banco de dados
            messages.success(request, 'Atividade cadastrada com sucesso!')
            return HttpResponseRedirect(reverse('lista-atividades')) # o reverse é para redirecionar para a página de lista de atividades

    form = AtividadesForm() # Cria um formulário vazio de atividades
    return render(request, 'cadastro_atividades.html', {'form': form}) # Retorna o formulário para o template


def criar_classe(request):
    if request.method == 'POST':
        form = ClassForm(request.POST) # o request.POST é para pegar os dados do formulário
        if form.is_valid():
            form = form.save(commit=False) # o commit=False é para não salvar no banco de dados ainda
            form.save() # Salva o objeto no banco de dados
            messages.success(request, 'Turma cadastrada com sucesso!')
            return HttpResponseRedirect(reverse('professor')) # o reverse é para redirecionar para a página de lista de atividades

    form = ClassForm() # Cria um formulário vazio de atividades
    return render(request, 'cadastro_turma.html', {'form': form}) # Retorna o formulário para o template


def lista_turmas(request):
    turmas = Classes.objects.all()  # Obtém todas as turmas do banco de dados
    return render(request, 'index_turma_professor.html', {'turmas': turmas})  # Passa as turmas para o template


def detalhes_atividade(request, id):
    atividade = Atividades.objects.get(id=id)
    context = {
        'atividade': atividade
    }
    return render(request, 'detalhes_atividades.html', context)


def detalhes_turma(request, id):
    template_name = 'detalhes_class.html'
    turma = Classes.objects.get(id=id)
    context = {
        'turma': turma
    }
    return render(request, template_name, context)


def turma_delete_page(request):
    turmas = Classes.objects.all()
    return render(request, 'delete_turma_page.html', {'turmas': turmas})


def atividade_delete_page(request):
    atividades = Atividades.objects.all()
    return render(request, 'delete_atividades_page.html', {'atividades': atividades})


def atividade_delete(request, id):
    atividade = Atividades.objects.get(id=id) # Pega o objeto no banco de dados
    if request.method == 'POST':
        atividade.delete() # Deleta o objeto
        messages.success(request, 'Atividade deletada com sucesso!')
        return HttpResponseRedirect(reverse('lista-atividades')) # Redireciona para a página de lista de atividades
    return render(request, 'index_turma_professor.html', {'atividade': atividade}) # Retorna o template de delete de atividades se 


def turma_delete(request, id):
    turma = Classes.objects.get(id=id) # Pega o objeto no banco de dados
    if request.method == 'POST':
        turma.delete() # Deleta o objeto
        messages.success(request, 'Classes deletada com sucesso!')
        return HttpResponseRedirect(reverse('lista-turmas'))
    return render(request, 'index_turma_professor.html', {'turma': turma})