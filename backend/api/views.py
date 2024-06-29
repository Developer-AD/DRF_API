from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student


class StudentModelViewsetAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
# -------------------- USING CONCRETE VIEW COMBINED CLASS END ------------------------------------------
