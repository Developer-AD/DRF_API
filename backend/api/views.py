from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView

from .models import Student
from .serializers import StudentSerializer


# ==================================== Write Your Code Here ==========================================




def home(request):
    return render(request, 'index.html')

# -------------------- USING GENERIC VIEWSETS COMBINED CLASS START -----------------------
class ListCreateStdAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class RetrieveUpdateStdAPI(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RetrieveUpdateDeleteStdAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
# -------------------- USING GENERIC VIEWSETS COMBINED CLASS END -------------------------





# # -------------------- USING GENERIC VIEWSETS INDIVIDUAL CLASS START ---------------------
# class ListStudentdAPI(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class CreateSudentAPI(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class UpdateStudentAPI(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class RetrieveStudentAPI(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class DestroyStudentAPI(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
# # -------------------- USING GENERIC VIEWSETS INDIVIDUAL CLASS END -----------------------

