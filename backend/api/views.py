from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Student
from .serializers import StudentSerializer



def home(request):
    return render(request, 'index.html')

# -------------------- USING CONCRETE VIEW COMBINED CLASS START -----------------------
class ListCreateStdAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class RetrieveUpdateDeleteStdAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
# -------------------- USING CONCRETE VIEW COMBINED CLASS END -------------------------
