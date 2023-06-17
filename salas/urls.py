from django.contrib import admin
from django.urls import path, include
from courses.views import SubjectViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet )

urlpatterns = [
    path('', include(router.urls)),
    path('authentications', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rooms', include('rooms.urls')),
    path('classes', include('classes.urls')),
    path('courses', include('courses.urls')),
    path('professor', include('professors.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
