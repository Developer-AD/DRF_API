from django.urls import path, include
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student-api', views.StudentModelViewsetAPI,
                basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]