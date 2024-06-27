from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status



def home(request):
    return render(request, 'index.html')

# -------------------- USING CONCRETE VIEW COMBINED CLASS START -----------------------
# class StudentModelViewsetAPI(viewsets.ModelViewSet):
class StudentModelViewsetAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
# -------------------- USING CONCRETE VIEW COMBINED CLASS END ------------------------------------------
