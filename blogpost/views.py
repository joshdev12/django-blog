from django.shortcuts import render, redirect

from post.forms import CommentForm

from post.models import Post
# Create your views here. 

def detail(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk)
    
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
           comment = form.save(commit=False)
           comment.post = post
           comment.save()
           
           return redirect('post_detail', post.pk)
    
    else:  
         form = CommentForm()          
    
    context = {"post":post, "form":form}
            
    return render(request, 'blogpost/detail.html', context, )
