from django.db import models

from login.models import User

# Create your models here.

class Repertory(models.Model):
    music_name = models.CharField(max_length=255, null=False, blank=False)
    music_artist = models.CharField(max_length=255, null=False, blank=False)
    music_album = models.CharField(max_length=255, null=False, blank=False)
    music_genre = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    who_added = models.ForeignKey(User, on_delete=models.PROTECT)
