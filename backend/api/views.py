# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



# ==================================== Write Your Code Here ==========================================
def home(request):
    return render(request, 'index.html')


def student_detail(request, id):
    print('---------------------- Student Details Start ------------------')
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student)

    # data = JSONRenderer().render(serializer.data)
    # return HttpResponse(data, content_type='application/json')
    return JsonResponse(serializer.data)  # safe=False not required for single.


def student_details(request):
    print('---------------------- Student Details Start ------------------')
    # student = Student.objects.get(id=2)
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)

    # data = JSONRenderer().render(serializer.data)
    # return HttpResponse(data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def student_api(request):
    # ------------------------------------ VIEW ------------------------------
    if request.method == 'GET':
        """
        You have to make a GET request with atleast
        empty `{}` Json data. Make request in thunder or requests. 
        """
        
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            
            return JsonResponse(serializer.data)
            return HttpResponse('Get single data.')

        # If Id id None then send all data.
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        
        return JsonResponse(serializer.data, safe=False)  # safe=False not required for single.

    # ------------------------------------ CTEATE ------------------------------
    if request.method == 'POST':
        json_data = request.body

        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Data inserted successfully..!', 'status': 200}
            return JsonResponse(response)

        return JsonResponse(serializer.errors)

# -------------------------------- PUT -------------------------------------------------
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)
        if id is not None:
            try:
                student = Student.objects.get(id=id)

                ''' partial=True : This will expect all fields to update otherwise you will
                    get All fields required.'''
                # serializer = StudentSerializer(student, data = python_data, partial=True) # partial update.
                # full update.
                serializer = StudentSerializer(student, data=python_data)

                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'msg': 'Data Udpated..!', 'status': 200})

                return JsonResponse(serializer.errors)
            except Student.DoesNotExist:
                return JsonResponse({'msg': "ID Doesn't Exists", 'status': 400})

# -------------------------------- PATCH -------------------------------------------------
    if request.method == 'PATCH':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)

        if id is not None:
            try:
                student = Student.objects.get(id=id)

                ''' partial=True : This will expect all fields to update otherwise you will
                    get All fields required.'''
                serializer = StudentSerializer(
                    student, data=python_data, partial=True)  # partial update.
                # serializer = StudentSerializer(student, data = python_data) # full update.

                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'msg': 'Data Udpated..!', 'status': 200})

                return JsonResponse(serializer.errors)
                    
            except Student.DoesNotExist:
                return JsonResponse({'msg': "ID Doesn't Exists", 'status': 400})
                
        return JsonResponse({'msg': 'ID Not Sent', 'status': 400})

# -------------------------------- DELETE ------------------------------------------
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        id = python_data.get('id', None)

        if id is not None:
            try:
                student = Student.objects.get(id=id)
                student.delete()
                return JsonResponse({'msg': 'Data Deleted..!', 'status': 200})
            except Student.DoesNotExist:
                return JsonResponse({'msg':"ID Doesn't Exists", 'status':400})
        return JsonResponse({'msg':'ID Not Sent', 'status':400})
