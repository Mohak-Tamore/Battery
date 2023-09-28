from.models import *
from rest_framework import serializers


# station serializer logic
class StationSerializer(serializers.Serializer):
    stationid = serializers.CharField(max_length=100)
    stationname = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    battery_available = serializers.IntegerField()
    avail_slots = serializers.IntegerField()
    battery_half = serializers.IntegerField()
    battery_ready = serializers.IntegerField()

    
    def create(self, validated_data):
        return Station.objects.create(**validated_data)

    def update(self, station, validated_data):
        newStation = Station(**validated_data)
        newStation.stationid = station.stationid
        newStation.save()
        return newStation
    
# Users serializers logic
class UsersSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    user_name = serializers.CharField(max_length=100)
    phone_no = serializers.IntegerField()
    email = serializers.EmailField()
    city = serializers.CharField(max_length=100)

    
    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, users, validated_data):
        newUsers = Users(**validated_data)
        newUsers.stationid = users.stationid
        newUsers.save()
        return newUsers
    

