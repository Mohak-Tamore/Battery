from rest_framework.decorators import api_view
from rest_framework.response import Response
import time
import threading

def decrease_battery():
    global number
    while number >= 0:
        print(f"Current Battery%: {number}")
        number -= 2
        time.sleep(300)

decrement_thread = threading.Thread(target=decrease_battery)
decrement_thread.start()



# api from here






