from django.db import models
from django.contrib.auth.models import User 

class Station(models.Model):
    sid = models.CharField(primary_key=True, max_length=100)
    address = models.TextField()
    half = models.IntegerField()
    name = models.TextField()
    no_available = models.IntegerField()
    no_slots = models.IntegerField()
    ready = models.IntegerField()


class Battery(models.Model):
    bid = models.CharField(primary_key=True, max_length=100)
    sid = models.ForeignKey(Station, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    current = models.IntegerField()
    cycles = models.IntegerField()
    kWh = models.FloatField()
       

class User(models.Model):
    user_id = models.CharField(max_length=50)
    user_name = models.TextField()
    city = models.TextField()
    contact = models.IntegerField()
    country = models.CharField(max_length=50)
    email = models.EmailField()