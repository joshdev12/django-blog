
import random as rd

from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request, *args, **kwargs):
    posts = Post.objects.all()
    rand_post = rd.choice(posts)
    rand_postone = rd.choice(posts)
    rand_posttwo = rd.choice(posts)
    rand_postthree = rd.choice(posts)
    caro = posts.order_by("-created")[:4]
    context = {"posts": posts, "caro": caro, "rand_post": rand_post, "rand_postone":rand_postone, "rand_posttwo":rand_posttwo, "rand_postthree":rand_postthree  }
  
    return render(request, 'post/index.html', context)


def post(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    context = {"form": form}
    
    if form.is_valid():
        user = form.save()
        user.creator = request.user
        user.save()
        return redirect("index")
    return render(request, 'post/post.html', context)
