from rest_framework import serializers
from login.serializers import UserSerializerList

from repetory.models import Repertory

class RepertorySerializer(serializers.ModelSerializer):
    who_added = UserSerializerList()
    class Meta:
        model = Repertory
        fields = [
            'id',
            'music_name',
            'music_artist',
            'music_album',
            'music_genre',
            'created_at',
            'who_added',
            ]
