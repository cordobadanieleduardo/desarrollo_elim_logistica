# Generated by Django 5.1.6 on 2025-02-18 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0026_alter_vehiculo_disponibilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 18, 0, 42, 28, 621461), null=True),
        ),
    ]
