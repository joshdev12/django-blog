from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = RichTextField()
    image = models.ImageField(blank=True, null=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    
    @property
    def image_url(self):
        try:
            url = self.image.url
        except ValueError: 
            url = "/media/dar.jpg"
        return url
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
      
    