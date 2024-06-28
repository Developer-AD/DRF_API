from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, id=None):
    # ------------------------------------ VIEW ------------------------------
    if request.method == 'GET':
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
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Data inserted successfully..!'}
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# -------------------------------- PUT -------------------------------------------------
    if request.method == 'PUT':
        if id is not None:
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student, data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    response = {'msg': 'Complete Data Updated Successfully..!'}
                    return Response(response, status=status.HTTP_200_OK)

                return Response(serializer.errors)

            except Student.DoesNotExist:
                return JsonResponse({"msg": "Student not found..!", 'status': 400})

# -------------------------------- PATCH -------------------------------------------------
    if request.method == 'PATCH':
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
    if request.method == 'DELETE':
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
