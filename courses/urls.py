from django.urls import path
from courses.views import CourseViewSet

app_name = 'courses'

# Criando rotas para o serializer de forma individual
urlpatterns = [
    path('/', CourseViewSet.as_view(actions={'get': 'list'}), name='course_list'),
    path('/<int:pk>', CourseViewSet.as_view(actions={'get': 'retrieve'}), name='course_details'),
    path('/create', CourseViewSet.as_view(actions={'post': 'create'}), name='course_create'),
    path('/<int:pk>/update', CourseViewSet.as_view(actions={'put': 'update'}), name='course_update'),
    path('/delete/<int:pk>', CourseViewSet.as_view(actions={'delete': 'destroy'}), name='course_delete'),
]
