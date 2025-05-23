from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Posts
from .forms import PostForm
from django.contrib import messages

@login_required
def home(request):
    posts = Posts.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def settings(request):
    return render(request, 'settings.html')

def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    
    if request.method == 'POST':
        # Opcional: Só o autor pode deletar
        if post.author == request.user:
            post.delete()
            messages.success(request, "Post deletado com sucesso.")
        else:
            messages.error(request, "Você não tem permissão para deletar este post.")
        return redirect('home')
    
    # Se for GET, pode redirecionar para o post_detail ou home (não permitir deletar por GET)
    return redirect('post_detail', post_id=post_id)