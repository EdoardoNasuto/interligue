# Generated by Django 3.2.8 on 2023-04-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0011_match_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='week',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
