from django.shortcuts import render
from rest_framework import viewsets

from repetory.models import Repertory
from repetory.serializers import RepertorySerializer

# Create your views here.
class RepertoryView(viewsets.ModelViewSet):
    queryset = Repertory
    serializer_class = RepertorySerializer

    def perform_create(self, serializer):
        breakpoint()
