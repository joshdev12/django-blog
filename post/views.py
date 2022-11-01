from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request, *args, **kwargs):
    posts = Post.objects.all()
    context = {"posts": posts}
    # profile = None 
    
    # context["profile"] = profile

    return render(request, 'post/index.html', context)
