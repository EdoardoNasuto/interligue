# Generated by Django 3.2.8 on 2023-06-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_auto_20230603_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('split', models.IntegerField(default='1')),
            ],
        ),
    ]