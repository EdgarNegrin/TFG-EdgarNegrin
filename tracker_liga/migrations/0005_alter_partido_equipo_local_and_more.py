# Generated by Django 4.1.7 on 2023-02-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_liga', '0004_remove_partido_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='equipo_local',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='partido',
            name='equipo_visitante',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
