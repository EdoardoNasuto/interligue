# Generated by Django 3.2.8 on 2023-04-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20230425_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
