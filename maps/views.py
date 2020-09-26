from django.views.generic import TemplateView
from .models import Facility, Checked


class IndexView(TemplateView):
    template_name = "maps/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        latest_facility_list = Facility.objects.order_by('-pub_date')[:5]
        context = {
        'latest_facility_list': latest_facility_list,
        }
        return context

class AreaView(TemplateView):
    template_name = "maps/area.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        latest_facility_list = Facility.objects.order_by('-pub_date')[:5]
        context = {
        'latest_facility_list': latest_facility_list,
        }
        return context
    
class RankingView(TemplateView):
    template_name = "maps/ranking.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        latest_facility_list = Facility.objects.order_by('-pub_date')[:5]
        context = {
        'latest_facility_list': latest_facility_list,
        }
        return context
    
class KeywordView(TemplateView):
    template_name = "maps/keyword.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        latest_facility_list = Facility.objects.order_by('-pub_date')[:5]
        context = {
        'latest_facility_list': latest_facility_list,
        }
        return context
    
class DetailView(TemplateView):
    template_name = "maps/details.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        latest_facility_list = Facility.objects.order_by('-pub_date')[:5]
        context = {
        'latest_facility_list': latest_facility_list,
        }
        return context