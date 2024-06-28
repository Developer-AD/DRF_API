from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication
from .permissions import CustomPermission
# -------------------- USING CONCRETE VIEW COMBINED CLASS START -----------------------
# class StudentModelViewsetAPI(viewsets.ModelViewSet):
class StudentModelViewsetAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermission]
# -------------------- USING CONCRETE VIEW COMBINED CLASS END --------------------------