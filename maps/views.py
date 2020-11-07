from django.views.generic import TemplateView
from reviews.models import Review
from .forms import ReviewCreateSimpleForm
from django.shortcuts import render, get_object_or_404, redirect


import googlemaps
import pprint # list型やdict型を見やすくprintするライブラリ

class IndexView(TemplateView):
    template_name = "maps/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        latest_review_list = Review.objects.all().order_by('-checked_number')
        context = {
            'review_list': latest_review_list,
        }
        return context

def AreaView(request):
    latest_review_list = Review.objects.all().order_by('-checked_number')
    form = ReviewCreateSimpleForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:review_list')

    context = {
        'review_list': latest_review_list,
        'form': form
    }

    return render(request, 'maps/area.html', context)



class RankingView(TemplateView):
    template_name = "maps/ranking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        latest_review_list = Review.objects.all().order_by('-checked_number')
        context = {
            'review_list': latest_review_list,
        }
        return context


class KeywordView(TemplateView):
    template_name = "maps/keyword.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        latest_review_list = Review.objects.all().order_by('-checked_number')
        context = {
            'review_list': latest_review_list,
        }
        return context


class DetailView(TemplateView):
    template_name = "maps/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        latest_review_list = Review.objects.all().order_by('-checked_number')
        context = {
            'latest_facility_list': latest_review_list,
        }
        return context

