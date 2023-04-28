# Generated by Django 4.2 on 2023-04-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, db_column='id', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='username', max_length=100)),
                ('email', models.EmailField(db_column='email', max_length=100)),
            ],
            options={
                'managed': False,
            },
        ),
    ]
