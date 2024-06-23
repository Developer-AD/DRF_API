from django.urls import path
from api import views

urlpatterns = [
    path('', views.home),
    path('stdinfo/', views.student_info),
    path('student-api/', views.student_api),
    path('student-api/<int:id>', views.student_api),
]
