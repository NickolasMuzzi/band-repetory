from rest_framework import serializers

from login.models import User

class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]
