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

    # 問題の箇所 2を任意の変数に

    context = {'review_list': Review.objects.all().order_by('-created_at'),
               'form': forms, }

    return render(request, 'menu/index.html', context)

def Countup(request, id):
    #    model = Review
    #    template_name = "menu/index.html"

    # 問題の箇所 2を任意の変数に
    review = Review.objects.get(pk=id)

    if request.method == 'POST':
        # データの新規追加
        review.checked_number += 1
        review.save()

    context = {'review_list': Review.objects.all().order_by('-created_at'),
                'checked_number' : Review.objects.get(pk=id).checked_number,
               'max_number': Review.objects.get(pk=id).max_number,
               'form': forms, }

    return render(request, 'menu/index.html', context)



class PostView(ListView):
    model = Review
    template_name = 'menu/new_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["checked_number"] = Review.objects.get(pk=2).checked_number  # 他のモデルからデータを取得
        return context


class Search(ListView):
    template_name = 'maps/keyword.html'
    model = Review

    def get_queryset(self, **kwargs):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Review.objects.filter(
                Q(store_name__icontains=q_word) | Q(store_area__icontains=q_word))
        else:
            object_list = Review.objects.all()
        return object_list

    """def search_context_data(self, **kwargs):
        context = super().search_context_data(**kwargs)
        context['review_list'] = model.objects.all()
        return context"""


# クラスベースに書き換え
"""def search(request):
    query = request.GET.get('q')

    #全施設から検索を行う

    if query:
        posts = Post.objects.all().order_by('-created_at')
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(user__username__icontains=query)
        ).distinct()
    else:
        posts = Review.objects.all().order_by('-created_at')

    return render(request, 'maps/keyword.html', {'posts': posts, 'query': query, })  # 省略"""
