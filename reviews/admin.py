from django.contrib import admin
from .models import Review,Participants, User

admin.site.register(Review)
admin.site.register(User)
admin.site.register(Participants)
# Register your models here.
