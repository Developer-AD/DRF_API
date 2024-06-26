from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import Student
from .serializers import StudentSerializer


# ==================================== Write Your Code Here ==========================================
def home(request):
    return render(request, 'index.html')

class StudentAPI(ListAPIView, RetrieveModelMixin):

    """
    In ListAPIView and CreateModelMixin not required PK.
    RetrieveModelMixin and UpdateModelMixin and DestroyModelMixin required PK.
    """
    
# # ------------------------------------ LIST VIEW ALL OBJ------------------------------
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

# # ------------------------------------ RETRIVE SINGLE OBJ ONLY ------------------------------
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
# # ------------------------------------ CTEATE ------------------------------
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

# # -------------------------------- PUT -------------------------------------------------
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    
# # -------------------------------- PATCH -------------------------------------------------
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    
# # -------------------------------- DELETE ------------------------------------------
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
