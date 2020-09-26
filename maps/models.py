from django.db import models


class Facility(models.Model):
    facility_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Checked(models.Model):
    facility_name = models.ForeignKey(Facility, on_delete=models.CASCADE)
    checked_number = models.IntegerField(default=0)