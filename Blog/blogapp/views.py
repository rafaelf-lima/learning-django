from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.
def lista_post(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'blogapp/lista_post.html', {'posts': posts})

def detalha_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blogapp/detalha_post.html', {'post': post})

@login_required
def cria_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalha_post', pk = post.pk)
    else:
        form = PostForm()

    return render(request, 'blogapp/cria_post.html', {'form': form})    
    

@login_required
def edita_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.autor:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalha_post', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blogapp/edita_post.html', {'form': form, 'post': post})


@login_required
def deleta_post(request,pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.autor:
        raise PermissionDenied
    
    if request.method == 'POST':
        post.delete()
        return redirect('lista_post')
        
    return render(request, 'blogapp/confirma_delete.html', {'post': post})


    