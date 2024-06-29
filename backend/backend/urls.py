from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('student-api', views.StudentModelViewsetAPI,
                basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify-token/', TokenVerifyView.as_view(), name='verify_token'),
]
