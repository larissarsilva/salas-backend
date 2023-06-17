from django.urls import path
from classes.views import ListCreateClassesView, UpdateDeleteClassesView

app_name = 'classes'

urlpatterns = [
    path('', ListCreateClassesView.as_view(), name='classes-list'),
    path('/<int:pk>', UpdateDeleteClassesView.as_view(), name='classes-details')
]
