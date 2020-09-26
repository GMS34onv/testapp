from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('reviews/', include('reviews.urls')),
    path('good/', include('good.urls')),
    path('menu/', include('menu.urls')),
    path('maps/', include('maps.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]