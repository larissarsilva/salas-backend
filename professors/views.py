from rest_framework import generics

from professors.models import Professor
from professors.serializers import ProfessorSerializer


class ListCreateProfessorView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class UpdateDeleteProfessorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer    