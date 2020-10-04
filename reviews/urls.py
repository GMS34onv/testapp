from django.urls import path
from maps.views import IndexView, DetailView
from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'reviews'
 
urlpatterns = [
    # ex: /maps/
    path('', views.review_list, name='review_list'), #　追加
    path('detail/<int:pk>', views.review_detail, name='review_detail'), #　追加
    path('create/', views.review_create, name='review_create'), #　追加
    path('update/<int:pk>/', views.review_update, name='review_update'),
    path('delete/<int:pk>/', views.review_delete, name='review_delete'),
    
]





