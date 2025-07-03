from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tarefa_list(request):
    if request.method == 'POST':
        titulo_da_tarefa = request.POST.get('titulo')
        if titulo_da_tarefa:
            Tarefa.objects.create(titulo=titulo_da_tarefa, usuario=request.user)
        return redirect('tarefa_list')
    
    
    tarefas = Tarefa.objects.filter(usuario=request.user)

    contexto = {
        'tarefas': tarefas
    }
    return render(request, 'tarefas/tarefa_list.html', contexto)

@login_required
def tarefa_update(request, pk):
    tarefa = get_object_or_404(Tarefa, id=pk)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('tarefa_list')

@login_required
def tarefa_delete(request, pk):
    tarefa = get_object_or_404(Tarefa, id=pk)
    tarefa.delete()
    return redirect('tarefa_list')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('tarefa_list')
    else:
        form = UserCreationForm()
    return render(request, 'tarefas/cadastro.html', {
        'form': form
    })
    
    
def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('tarefa_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tarefas/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('tarefa_list')