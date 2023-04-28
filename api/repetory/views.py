
from rest_framework import viewsets
from rest_framework import  response
from repetory.services.google_search import GoogleSearch

from repetory.models import Repertory
from repetory.serializers import RepertorySerializer
from rest_framework.decorators import action

class RepertoryView(viewsets.ModelViewSet):
    queryset = Repertory.objects.all()
    serializer_class = RepertorySerializer


    @action(methods=['POST'], detail=False)
    def search_song(self, request):
        query = request.data['pesquisa']
        pesquisa = GoogleSearch(query).search()
        return response.Response(status=200, data=pesquisa)
