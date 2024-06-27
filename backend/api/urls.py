from django.urls import path
from api import views

urlpatterns = [
    path('', views.home),
    # path('student-api/', views.ListCreateStdAPI.as_view()),
    # path('student-api/<int:pk>', views.RetrieveUpdateDeleteStdAPI.as_view()),

# -------------------- USING GENERIC VIEWSETS COMBINED CLASS -----------------------
    path('student-api/', views.ListCreateStdAPI.as_view()),
    # path('student-api/<int:pk>', views.RetrieveUpdateStdAPI.as_view()),
    path('student-api/<int:pk>', views.RetrieveUpdateDeleteStdAPI.as_view()),



# -------------------- USING GENERIC VIEWSETS INDIVIDUAL CLASS -----------------------
    # path('student-api/', views.ListStudentdAPI.as_view()),
    # path('student-api/', views.CreateSudentAPI.as_view()),

    # path('student-api/<int:pk>', views.RetrieveStudentAPI.as_view()),
    # path('student-api/<int:pk>', views.UpdateStudentAPI.as_view()),
    # path('student-api/<int:pk>', views.DestroyStudentAPI.as_view()),
]
