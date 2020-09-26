from django.urls import path
from maps.views import IndexView, DetailView
from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'good'
 
urlpatterns = [
    # ex: /maps/
    path('', views.IndexView.as_view(),name="index"),
#    path('count/', views.CountView.as_view(), name='count'),
    path('count/', views.count, name='count'),
]