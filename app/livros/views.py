from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import api_view
from rest_framework import Response
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
