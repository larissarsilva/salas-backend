from django.shortcuts import render
from rest_framework import viewsets, generics
from courses.models import Course, Subject
from .serializers import CourseSerializer, SubjectSerializer
# Definir o viewset do serializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
