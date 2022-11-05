
from django import forms 

from post.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body", "image")
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ("name", "email", "body")   