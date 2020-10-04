from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Post, Category, User
from reviews.models import Review, Facilities
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from accounts import forms


def IndexView(request):
#    model = Review
#    template_name = "menu/index.html"
    
    participants = Review.objects.get(pk=2)
    
    if request.method == 'POST':
        # データの新規追加
        participants.checked_number += 1
        participants.save()
    
    context = {
        'review_list' : Review.objects.all().order_by('-created_at'),
        'checked_number' : Review.objects.get(pk=2).checked_number,
        'max_number' : Review.objects.get(pk=2).max_number,
        'form' : forms,
    }

    return render(request, 'menu/index.html', context)
 
class PostView(ListView):
    model = Review
    template_name = 'menu/new_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["checked_number"] = Review.objects.get(pk=2).checked_number # 他のモデルからデータを取得
        return context

def search(request):
    query = request.GET.get('q')
    
    if query:
        posts = Post.objects.all().order_by('-created_at')
        posts = posts.filter(
            Q(title__icontains=query)|
            Q(user__username__icontains=query)
            ).distinct()
    else:
        posts = Post.objects.all().order_by('-created_at')
        
    return render(request, 'blog_app/index.html', {'posts': posts, 'query': query,}) #省略