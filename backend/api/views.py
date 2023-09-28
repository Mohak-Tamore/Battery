from django.shortcuts import render, HttpResponse

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status


# APi related imports
from .models import *
from .serializer import *



def home(request):
    return HttpResponse("Project started")

# import time
# import threading

# def decrease_battery():
#     global number
#     while number >= 0:
#         print(f"Current Battery%: {number}")
#         number -= 2
#         time.sleep(300)

# decrement_thread = threading.Thread(target=decrease_battery)
# decrement_thread.start()








# api from here

# 1.Station

@csrf_exempt
def stationview(request):
    if request.method == 'GET':
        emp = Station.objects.all()
        so = StationSerializer(emp, many=True)
        return JsonResponse(so.data, safe=False)
    
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = StationSerializer(data= jsonData)
        if serializer.is_valid():
            station_instance = serializer.save()  # Save the instance and get the saved object
            return JsonResponse(serializer.data, safe=False)
        
        else:
            return JsonResponse(serializer.errors , safe=False)
        

@csrf_exempt
def stationdetailview(request, pk):

    try:
        station = Station.objects.get(stationid=pk)
    
    except Station.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == 'DELETE':
        station.delete()
        return HttpResponse(status= 202)


    elif request.method == 'GET':
        serializer = StationSerializer(station)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'PUT':
        jsonData = JSONParser().parse(request)
        serializer = StationSerializer(station, data= jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , safe=False)
        
        else:
            return JsonResponse(serializer.errors , safe=False)
        


# 2.Users

@csrf_exempt
def usersview(request):
    if request.method == 'GET':
        emp = Users.objects.all()
        so = UsersSerializer(emp, many=True)
        return JsonResponse(so.data, safe=False)
    
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = UsersSerializer(data= jsonData)
        if serializer.is_valid():
            users_instance = serializer.save()  # Save the instance and get the saved object
            return JsonResponse(serializer.data, safe=False)
        
        else:
            return JsonResponse(serializer.errors , safe=False)
        

@csrf_exempt
def usersdetailview(request, pk):

    try:
        users = Users.objects.get(usersid=pk)
    
    except Users.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == 'DELETE':
        users.delete()
        return HttpResponse(status= 202)


    elif request.method == 'GET':
        serializer = UsersSerializer(users)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'PUT':
        jsonData = JSONParser().parse(request)
        serializer = UsersSerializer(users, data= jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , safe=False)
        
        else:
            return JsonResponse(serializer.errors , safe=False)
        

