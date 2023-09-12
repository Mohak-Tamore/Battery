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

# @csrf_exempt
# def employeeview(request):
#     if request.method == 'GET':
#         emp = Employee.objects.all()
#         so = EmployeeSerializer(emp, many=True)
#         return JsonResponse(so.data, safe=False)
    
#     elif request.method == 'POST':
#         jsonData = JSONParser().parse(request)
#         serializer = EmployeeSerializer(data= jsonData)
#         if serializer.is_valid():
#             employee_instance = serializer.save()  # Save the instance and get the saved object
#             return JsonResponse(serializer.data, safe=False)
        
#         else:
#             return JsonResponse(serializer.errors , safe=False)
        
#         # return JsonResponse({"message":"done"}, safe=False)
#     # return JsonResponse({'soham':'nancy'})

# def userview(request):
#     emp = User.objects.all()
#     so = UserSerializer(emp, many=True)
#     return JsonResponse(so.data, safe=False)


# @csrf_exempt
# def employeedetailview(request, pk):

#     try:
#         employee = Employee.objects.get(pk=pk)
    
#     except Employee.DoesNotExist:
#         return HttpResponse(status=404)


#     if request.method == 'DELETE':
#         employee.delete()
#         return HttpResponse(status= 202)


#     elif request.method == 'GET':
#         serializer = EmployeeSerializer(employee)
#         return JsonResponse(serializer.data, safe=False)


#     elif request.method == 'PUT':
#         jsonData = JSONParser().parse(request)
#         serializer = EmployeeSerializer(employee, data= jsonData)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data , safe=False)
        
#         else:
#             return JsonResponse(serializer.errors , safe=False)
        






