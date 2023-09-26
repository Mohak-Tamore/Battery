from django.shortcuts import render, HttpResponse
import time
import threading

# def decrease_battery():
#     global number
#     while number >= 0:
#         print(f"Current Battery%: {number}")
#         number -= 2
#         time.sleep(300)

# decrement_thread = threading.Thread(target=decrease_battery)
# decrement_thread.start()

def home(request):
    return HttpResponse("Project started")


# api from here
