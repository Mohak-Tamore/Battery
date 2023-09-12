from.models import *
from rest_framework import serializers

class StationSerializer(serializers.Serializer):
    
    sid = serializers.CharField(primary_key=True, max_length=100)
    address = serializers.TextField()
    half = serializers.IntegerField()
    name = serializers.TextField()
    no_available = serializers.IntegerField()
    no_slots = serializers.IntegerField()
    ready = serializers.IntegerField()


    def create(self, validated_data):
        return Station.objects.create(**validated_data)

    def update(self, Stations, validated_data):
        newStation = Station(**validated_data)
        newStation.id = Stations.id
        newStation.save()
        return newStation
    


class BatterySerializer(serializers.Serializer):
    
    user_id = serializers.CharField(max_length=50)
    user_name = serializers.TextField()
    city = serializers.TextField()
    contact = serializers.IntegerField()
    country = serializers.TextField(max_length=50)
    email = serializers.EmailField()


    def create(self, validated_data):
        return Battery.objects.create(**validated_data)

    def update(self, battery, validated_data):
        newBattery = Battery(**validated_data)
        newBattery.id = battery.id
        newBattery.save()
        return newBattery
    
















class UserSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=50)
    user_name = serializers.TextField()
    city = serializers.TextField()
    contact = serializers.IntegerField()
    country = serializers.TextField(max_length=50)
    email = serializers.EmailField()   

