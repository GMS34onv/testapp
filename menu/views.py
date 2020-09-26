from django.views.generic import TemplateView, ListView
from .models import Post, Category
from reviews.models import Review, Facilities

class IndexView(ListView):
    model = Review
    template_name = "menu/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["checked_number"] = Review.objects.get(pk=1).checked_number # 他のモデルからデータを取得
        return context
 
class PostView(ListView):
    model = Review
    template_name = 'menu/new_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["checked_number"] = Review.objects.get(pk=1).checked_number # 他のモデルからデータを取得
        return context