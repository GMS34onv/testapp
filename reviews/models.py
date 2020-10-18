from django.utils import timezone
from django.db import models

# Create your models here.


class Review(models.Model):
    STARS = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
        
        )
    
    store_name = models.CharField('店名', max_length=255)
    text = models.TextField('口コミテキスト', blank=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    limit_date = models.DateTimeField('集合時間', default=timezone.now)
    checked_number = models.IntegerField(default=0)
    max_number = models.IntegerField(default=30)
    
    def __str__(self):
        return self.title

class User(models.Model):
    GENDER = (
        ('男', '男'),
        ('女', '女'),
        
    )
    
    gender = models.CharField('性別', choices=GENDER, max_length=10)
    
class Participants(models.Model):
    name = models.CharField('ユーザー名', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)
#    facility = models.ForeignKey(Review, on_delete=models.CASCADE)
    

class Facilities(models.Model):
    STARS = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
        
        )
    
    store_name = models.CharField('店名', max_length=255)
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('口コミテキスト', blank=True)
    stars = models.IntegerField('星の数', choices=STARS)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    checked_number = models.IntegerField(default=0)
    max_number = models.IntegerField(default=30)
    total_number = models.IntegerField(default=30)
    
    def __str__(self):
        return self.title
