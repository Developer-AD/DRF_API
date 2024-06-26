from django.urls import path
from api import views

urlpatterns = [
    path('', views.home),
    path('student-api/', views.ListCreateStdAPI.as_view()),
    path('student-api/<int:pk>', views.RetrieveUpdateDeleteStdAPI.as_view()),
]
