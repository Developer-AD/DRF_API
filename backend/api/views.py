from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# -------------------- USING CONCRETE VIEW COMBINED CLASS START -----------------------
# class StudentModelViewsetAPI(viewsets.ModelViewSet):
class StudentModelViewsetAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Authentication and permission classes can be defined here as well.
    # If you want to use this authentication and permission classes, for many classes, you can define them in settings.py.

    authentication_classes = [BasicAuthentication] # Default is AllowAny.
    permission_classes = [IsAuthenticated] # Only authenticated users can access the API.
    # permission_classes = [IsAdminUser] # Allow only user with Staff Status True.

    # Override Global permission classes of settings.py.
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]

# -------------------- USING CONCRETE VIEW COMBINED CLASS END ------------------------------------------