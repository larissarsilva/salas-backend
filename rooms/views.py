from django.shortcuts import render
from .models import Block, Room
from rest_framework import generics
from .serializers import BlockSerializer, RoomSerializer

# Criando as views separadas com generics
class ListCreateBlockView(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class UpdateDeleteBlockView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer