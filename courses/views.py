from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from courses.models import Course, Subject
from .serializers import CourseSerializer, SubjectSerializer
from rest_framework.response import Response
from rest_framework import status
# Definir o viewset do serializer

class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
