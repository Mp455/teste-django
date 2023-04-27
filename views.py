from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Post
from .models import Comment
from django.contrib import messages
from .forms import CommentForm
from django.utils import timezone
# Create your views here.
def blog(request):
    postagem = Post.objects.all()
    comentario = Comment.objects.all()
    context = {
        'postagens': postagem,
        'comentarios': comentario,
    }
    return render(request, 'blog-template.html', context)

from django.utils import timezone

# ...

def detalhe(request, post_id):
    postagem = get_object_or_404(Post, id=post_id)
    comentario = Comment.objects.filter(post=postagem)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = postagem
            comentario.pub_date = timezone.now()  # adiciona a data atual
            comentario.save()
            messages.success(request, 'Comentário foi inserido com sucesso!')
            return redirect('blog')

    context = {
        'postagem': postagem,
        'comentarios': comentario,
        'form': form
    }
    return render(request, 'detalhe.html', context)


