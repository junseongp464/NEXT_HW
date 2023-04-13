from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models. CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    body = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
      return self.author
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.CharField(max_length=50)
    body = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
      return self.author
