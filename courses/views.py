from django.shortcuts import render
from rest_framework import viewsets
from courses.models import Course
from .serializers import CourseSerializer
# Definir o viewset do serializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
