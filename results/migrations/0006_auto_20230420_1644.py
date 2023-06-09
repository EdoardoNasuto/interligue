# Generated by Django 3.2.8 on 2023-04-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20230420_1610'),
        ('results', '0005_match_team_a_player_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='date',
        ),
        migrations.AddField(
            model_name='match',
            name='team_A_player_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_A_player_2', to='teams.player'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_A_player_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_A_player_3', to='teams.player'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_A_player_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_A_player_4', to='teams.player'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_A_player_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_A_player_5', to='teams.player'),
        ),
    ]
