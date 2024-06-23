from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer


# ==================================== Write Your Code Here ==========================================
def home(request):
    return render(request, 'index.html')

    # ------------------------------------ VIEW ------------------------------
class StudentAPI(APIView):
    def get(self, request,id=None, format=None):
        if id is not None:
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student)

                return Response(serializer.data)
            except Student.DoesNotExist:
                response = {'msg': 'Student not found..!'}
                return Response(response, status=status.HTTP_404_NOT_FOUND)

        # If Id id None then send all data.
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        # safe=False not required for single.
        return Response(serializer.data)

    # ------------------------------------ CTEATE ------------------------------
    def post(self, request, format=None):
        """
        request.data = Returns parsed JSON data from the request body.
        or
        request.POST = Returns POST data from the request body.
        
        request.method = Returns the HTTP method of the request (e.g., 'GET', 'POST
        request.query_params = Returns query parameters from the request URL.
        request.GET --> request.query_params.get('key', default_value) [standard]
        """
        
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Data inserted successfully..!'}
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------- PUT -------------------------------------------------
    def put(self, request, id, format=None):
        if id is not None:
            try:
                student = Student.objects.get(id=id)
                ''' partial=True : This will expect all fields to update otherwise you will
                    get All fields required.'''
              
                serializer = StudentSerializer(student, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    response = {'msg': 'Complete Data Updated Successfully..!'}
                    return Response(response, status=status.HTTP_200_OK)

                return Response(serializer.errors)

            except Student.DoesNotExist:
                return JsonResponse({"msg": "Student not found..!", 'status': 400})

# -------------------------------- PATCH -------------------------------------------------
    def patch(self, request, id, format=None):
        if id is not None:
            try:
                student = Student.objects.get(id=id)

                serializer = StudentSerializer(
                    student, data=request.data, partial=True)  # partial update.

                if serializer.is_valid():
                    serializer.save()
                    response = {'msg': 'Data Updated Successfully..!'}
                    return Response(response, status=status.HTTP_200_OK)

                return Response(serializer.errors)

            except Student.DoesNotExist:
                response = {"msg": "Student not found..!"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        return Response({'msg': 'ID Not Sent'}, status=status.HTTP_400_BAD_REQUEST)
        

# -------------------------------- DELETE ------------------------------------------
    def delete(self, request, id, format=None):
        if id is not None:
            try:
                student = Student.objects.get(id=id)
                student.delete()
                response = {'msg': 'Data Deleted Successfully..!'}
                return Response(response, status=status.HTTP_200_OK)

            except Student.DoesNotExist:
                response = {"msg": "Student not found..!"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        response = {'msg': 'ID Not Sent'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
