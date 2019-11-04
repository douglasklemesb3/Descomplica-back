from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from curso.models import Curso
from curso.serialaizers import CursoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

