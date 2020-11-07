from django.urls import path
from maps.views import IndexView, DetailView
from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'maps'
 
urlpatterns = [
    # ex: /maps/
    path('', views.IndexView.as_view(),name="index"),
    path('area/', views.AreaView, name='area'),
    path('ranking/', views.RankingView.as_view(), name='ranking'),
    path('keyword/', views.KeywordView.as_view(), name='keyword'),
    path('details/', views.DetailView.as_view(), name='details'),
    path('details/<int:facility_id>/', views.DetailView.as_view(), name='details'),
]