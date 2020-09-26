from django.db import models


class Participants(models.Model):
    checked_number = models.IntegerField(default=0)