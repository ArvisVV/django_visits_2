from django.db import models


class Room(models.Model):
    description = models.CharField(max_length=125)


class Visit(models.Model):

    name = models.CharField(max_length=125)
    date = models.CharField(max_length=10)
    reason = models.CharField(max_length=125)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)