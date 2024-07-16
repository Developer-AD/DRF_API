from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .customPagi import CustomPagination, CustomLimitOffsetPagination, CustomCursorPagination

class StudentModelViewsetAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]


# ------------------------------ Custom Filter Functionality ----------------------------------
    pagination_class = CustomPagination

# ------------------------------ LimitOffsetPagination Functionality ----------------------------------
    # pagination_class = CustomLimitOffsetPagination

# ------------------------------ CursorPagination Functionality ----------------------------------
    # pagination_class = CustomCursorPagination
    
