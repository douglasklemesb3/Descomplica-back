from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from entretenimentos.models import Entretenimento
from entretenimentos.serializers import EntretenimentoSerializer


class EntretenimentoViewSet(viewsets.ModelViewSet):
    queryset = Entretenimento.objects.all()
    serializer_class = EntretenimentoSerializer

