from django.shortcuts import render
from .models import Block, Room
from rest_framework import generics
from .serializers import BlockSerializer, RoomSerializer
from rest_framework.response import Response
from rest_framework import status

# Criando as views separadas com generics
class ListCreateBlockView(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class UpdateDeleteBlockView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class ListCreateRoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    # Sobrescrever list para retornar o statuscode personalizado
    # pode ser utilizado  Room.objects.all() ou self.get_queryset(), mas o self. é mais recomendado pq é mais flexivel
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = RoomSerializer(queryset, many = True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)