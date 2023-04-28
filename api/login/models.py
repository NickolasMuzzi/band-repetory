from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, db_column="id")
    username = models.CharField(max_length=100, db_column="username")
    email = models.EmailField(max_length=100, db_column="email")

    class Meta:
        managed = False
        db_table = "auth_user"
