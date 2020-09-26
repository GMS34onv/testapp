from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Participants
from django.shortcuts import get_object_or_404, render


class IndexView(TemplateView):
    template_name = "good/index.html"

class CountView(TemplateView):
    template_name = "good/good.html"


def count(request):
    """いいねボタンをクリック."""
    participants = get_object_or_404(Participants)

    if request.method == 'POST':
        # データの新規追加
        participants.checked_number += 1
        participants.save()
    
    checked_number = Participants.objects.get(pk=1).checked_number

    return render(request, 'good/good.html', {'checked_number': checked_number})