# here is the code for CRUD

@csrf_exempt
def employeeview(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        so = EmployeeSerializer(emp, many=True)
        return JsonResponse(so.data, safe=False)
    
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(data= jsonData)
        if serializer.is_valid():
            employee_instance = serializer.save()  # Save the instance and get the saved object
            return JsonResponse(serializer.data, safe=False)
        
        else:
            return JsonResponse(serializer.errors , safe=False)
        
        # return JsonResponse({"message":"done"}, safe=False)
    # return JsonResponse({'soham':'nancy'})

def userview(request):
    emp = User.objects.all()
    so = UserSerializer(emp, many=True)
    return JsonResponse(so.data, safe=False)


@csrf_exempt
def employeedetailview(request, pk):

    try:
        employee = Employee.objects.get(pk=pk)
    
    except Employee.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status= 202)


    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'PUT':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data= jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , safe=False)
        
        else:
            return JsonResponse(serializer.errors , safe=False)
        






