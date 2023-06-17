from rest_framework import generics

from classes.models import Classes
from classes.serializers import ClassesSerializer

class ListCreateClassesView(generics.ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer


class UpdateDeleteClassesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
