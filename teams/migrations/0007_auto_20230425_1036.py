# Generated by Django 3.2.8 on 2023-04-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_player_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='assists',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='saves',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='shots',
            field=models.IntegerField(default=0),
        ),
    ]
