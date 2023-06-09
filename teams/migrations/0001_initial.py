# Generated by Django 3.2.8 on 2023-04-19 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('tracker', models.URLField()),
                ('MMR', models.IntegerField(default=0)),
                ('goals', models.IntegerField(default=0)),
                ('saves', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('shots', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(default=1)),
                ('acronym', models.CharField(max_length=4)),
                ('league', models.IntegerField(default=1)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('player1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_player1', to='teams.player')),
                ('player2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_player2', to='teams.player')),
                ('player3', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_player3', to='teams.player')),
                ('player4', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_player4', to='teams.player')),
                ('player5', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_player5', to='teams.player')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
