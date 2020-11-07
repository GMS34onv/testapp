from django.urls import path, include
from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'pay'

urlpatterns = [
    path("", views.PayView.as_view(), name="pay_view")
]
