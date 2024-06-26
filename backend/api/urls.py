from django.urls import path
from api import views

urlpatterns = [
    path('', views.home),
    # path('student-api/', views.StudentAPI.as_view()),
    path('student-api/<int:pk>', views.StudentAPI.as_view()),
]
