from django.urls import path
from api import views

urlpatterns = [
    path('', views.home),
    path('stdinfo/<int:id>/', views.student_detail),
    path('student-api/', views.student_api),
    path('stdinfo/', views.student_details),
]
