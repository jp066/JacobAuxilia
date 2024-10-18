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
    return render(request, 'index_professor.html', {'nome_professor': username})


@login_required
def lista_atividades(request):
    atividades = Atividades.objects.all()
    context = {
        'atividades': atividades
        }
    return render(request, 'index_atividades.html', context=context)


@login_required
def lista_turmas(request):
    classes = Classes.objects.all()
    context = {
        'turmas': classes # turmas é o nome da variável que será usada no template
        }
    return render(request, 'index_atividades.html', context=context)


def criar_atividade(request):
    if request.method == 'POST':
        formAtv = AtividadesForm(request.POST) # o request.POST é para pegar os dados do formulário
        if form.is_valid():
            form = form.save(commit=False) # o commit=False é para não salvar no banco de dados ainda
            form.save() # Salva o objeto no banco de dados
            messages.success(request, 'Atividade cadastrada com sucesso!')
            return HttpResponseRedirect(reverse('listar_atividades')) # o reverse é para redirecionar para a página de lista de atividades

    form = AtividadesForm() # Cria um formulário vazio de atividades
    return render(request, 'cadastro_atividades.html', {'form': form}) # Retorna o formulário para o template


def criar_classe(request):
    if request.method == 'POST':
        form = ClassForm(request.POST) # o request.POST é para pegar os dados do formulário
        if form.is_valid():
            form = form.save(commit=False) # o commit=False é para não salvar no banco de dados ainda
            form.save() # Salva o objeto no banco de dados
            messages.success(request, 'Turma cadastrada com sucesso!')
            return HttpResponseRedirect(reverse('listar_atividades')) # o reverse é para redirecionar para a página de lista de atividades

    form = ClassForm() # Cria um formulário vazio de atividades
    return render(request, 'cadastro_atividades.html', {'form': form}) # Retorna o formulário para o template


def detalhes_atividade(request, id):
    template_name = 'detalhes_atividades.html'
    atividade = Atividades.objects.get(id=id)
    context = {
        'atividade': atividade
    }
    return render(request, template_name, context)


def detalhes_turma(request, id):
    template_name = 'detalhes_class.html'
    turma = Classes.objects.get(id=id)
    context = {
        'turma': turma
    }
    return render(request, template_name, context)


def update_atividade(request, id):
    atividade = get_object_or_404(Atividades, id=id)
    form = AtividadesForm(request.POST or None, instance=atividade)
    if form.is_valid():
        form.save()
        messages.success(request, 'Atividade atualizada com sucesso!')
        return HttpResponseRedirect(reverse('detalhes-atividades', args=[atividade.id]))
    return render(request, 'cadastro_atividades.html', {'form': form})


def update_turma(request, id):
    turma = get_object_or_404(Classes, id=id)
    form = ClassForm(request.POST or None, instance=turma)
    if form.is_valid():
        form.save()
        messages.success(request, 'Turma atualizada com sucesso!')
        return HttpResponseRedirect(reverse('detalhes_class', args=[turma.id]))
    return render(request, 'cadastro_turma.html', {'form': form})


def atividade_delete(request, id):
    atividade = Atividades.objects.get(id=id) # Pega o objeto no banco de dados
    if request.method == 'POST':
        atividade.delete() # Deleta o objeto
        messages.success(request, 'Atividade deletada com sucesso!')
        return HttpResponseRedirect(reverse('atividades-list'))
    return render(request, 'delete_atividades.html', {'atividade': atividade})


def turma_delete(request, id):
    turma = Classes.objects.get(id=id) # Pega o objeto no banco de dados
    if request.method == 'POST':
        turma.delete() # Deleta o objeto
        messages.success(request, 'Classes deletada com sucesso!')
        return HttpResponseRedirect(reverse('atividades-list'))
    return render(request, 'delete_turma.html', {'turma': turma})