# Generated by Django 3.2.8 on 2023-04-20 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_match_team_a_player_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='team_A_player_1',
        ),
    ]
