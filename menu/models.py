from django.contrib.auth.models import User
from django.db import models
 
class Category(models.Model):
    """カテゴリー"""
  
    name = models.CharField(max_length=255)
  
    def __str__(self):
        return self.name
  
  
class Post(models.Model):
    """ブログのポスト"""
  
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.title