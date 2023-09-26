from django.db import models

class Station(models.Model):
    stationid = models.TextField(primary_key=True)
    stationname = models.TextField()
    address = models.TextField()
    battery_available = models.IntegerField()
    avail_slots = models.IntegerField()
    battery_half = models.IntegerField()
    battery_ready = models.IntegerField()


class Users(models.Model):
    user_id = models.TextField(primary_key=True)
    user_name = models.TextField()
    phone_no = models.IntegerField()
    email = models.EmailField()
    city = models.TextField()

class Battery(models.Model):
    batteryid = models.TextField(primary_key=True)
    stationid = models.ForeignKey(Station, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    current = models.IntegerField()
    power = models.IntegerField()
    status = models.TextField()
    cycles = models.IntegerField()
       