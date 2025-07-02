from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

# Create your views here.
def tarefa_list(request):
    if request.method == 'POST':
        titulo_tarefa = request.POST.get('titulo')
        if titulo_tarefa:
            Tarefa.objects.create(titulo = titulo_tarefa)
        return redirect('tarefa_list')
    
    tarefas = Tarefa.objects.all()

    contexto = {
        'tarefas': tarefas
    }

    return render(request, 'tarefas/tarefa_list.html', contexto)

def tarefa_update(request, pk):
    tarefa = get_object_or_404(Tarefa, id=pk)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('tarefa_list')

def tarefa_delete(request, pk):
    tarefa = get_object_or_404(Tarefa, id=pk)
    tarefa.delete()
    return redirect('tarefa_list')

    
    
    

