from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class StudentModelViewsetAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()

    serializer_class = StudentSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(user=user)

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'city']

    filter_backends = [SearchFilter]
    # search_fields = ['name', 'city']
    search_fields = ['^name'] # Starts with case insensitive.
    # search_fields = ['=name'] # exact match.


    
