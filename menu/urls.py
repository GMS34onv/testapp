from django.urls import path
from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'menu'
 
urlpatterns = [
    # ex: /maps/
    path('', views.IndexView.as_view(),name="index"),
    path('new/', views.PostView.as_view(),name="new_list"),
    
]