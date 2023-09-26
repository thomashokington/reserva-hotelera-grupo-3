# Generated by Django 4.2.5 on 2023-09-26 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_habitacion_fecha_disponible_fin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitacion',
            name='fecha_disponible_fin',
        ),
        migrations.RemoveField(
            model_name='habitacion',
            name='fecha_disponible_inicio',
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
    ]
