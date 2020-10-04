from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Facilities, Participants
from .forms import ReviewCreateForm
from django.contrib.auth.models import User

# Create your views here.


def review_list(request):
    
    participants = Review.objects.get(pk=2)
    
    if request.method == 'POST':
        # データの新規追加
        participants.checked_number += 1
        participants.save()
    
    context = {
        'review_list' : Review.objects.all().order_by('-created_at'),
        'checked_number' : Review.objects.get(pk=2).checked_number,
        'max_number' : Review.objects.get(pk=2).max_number,
    }

    return render(request, 'reviews/review_list.html', context)


def review_detail(request, pk):
    context = {
        'review' : get_object_or_404(Review, pk=pk),
        'checked_number' : Review.objects.get(pk=pk).checked_number,
        'max_number' : Review.objects.get(pk=pk).max_number,
    }

    return render(request, 'reviews/review_detail.html' , context)

def review_create(request):


    form = ReviewCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:review_list')
  
    context = {
        'form': form
        
        }
    return render(request, 'reviews/review_form.html', context)

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    
    if request.method == 'POST':
        review.delete()
        return redirect('reviews:review_list')

    context = {
            'review' : review,
    }
    return render(request, 'reviews/review_confirm_delete.html', context)

def review_create_send(request):
    form = ReviewCreateForm(request.POST)
    if form.is_valid():
        
        form.save()
        return redirect('reviews:review_list')
    else:
        context = {
            'form' : form,
        }
        return render(request, 'reviews/review_form.html', context)

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    form = ReviewCreateForm(request.POST or None, instance=review)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:review_list')

    context = {
            'form' : form,
    }
    return render(request, 'reviews/review_form.html', context)

def count(request):
    """いいねボタンをクリック."""
    participants = get_object_or_404(Review)
    facilities = get_object_or_404(Facilities)
    if request.method == 'POST':
        # データの新規追加
        participants.checked_number += 1
        participants.save()
        
        facilities.total_number += 1
        facilities.save()
    
    checked_number = Review.objects.get(pk=1).checked_number

    return render(request, 'reviews/review_list.html', {'checked_number': checked_number})