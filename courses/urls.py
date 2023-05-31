from django.urls import path
from courses.views import CourseViewSet

app_name = 'courses'

# Criando rotas para o serializer de forma individual
urlpatterns = [
    path('/', CourseViewSet.as_view(actions={'get': 'list'}), name='course_list'),
    path('/create', CourseViewSet.as_view(actions={'post': 'create'}), name='course_create'),
    path('/<int:pk>', CourseViewSet.as_view(actions={'post': 'create'}), name='course_create'),
    path('/delete/<int:pk>', CourseViewSet.as_view(actions={'delete': 'destroy'}), name='course_delete'),
]
