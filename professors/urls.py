from django.urls import path
from professors.views import ListCreateProfessorView, UpdateDeleteProfessorView

app_name = 'professors'

urlpatterns = [
    path('', ListCreateProfessorView.as_view(), name='professor_list'),
    path('/<int:pk>', UpdateDeleteProfessorView.as_view(), name='professor_details'),
]
