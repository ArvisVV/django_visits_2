from django.db import models


class Visit(models.Model):

    name = models.CharField(max_length=125)
    date = models.CharField(max_length=10)
    reason = models.CharField(max_length=125)
