from.models import *
from rest_framework import serializers

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

    # def update(self, station, validated_data):
    #     newStation = Station(**validated_data)
    #     newStation.stationid = station.stationid
    #     newStation.save()
    #     return newStation
    

