# Generated by Django 4.2 on 2023-04-28 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repertory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=255)),
                ('music_artist', models.CharField(max_length=255)),
                ('music_album', models.CharField(max_length=255)),
                ('music_genre', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('who_added', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.user')),
            ],
        ),
    ]
