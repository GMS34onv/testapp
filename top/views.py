from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.views import generic

class IndexView(TemplateView):
    template_name = "top/index.html"
    