# Generated by Django 5.1.6 on 2025-02-20 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0046_alter_registro_fecha_alter_vehiculo_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 19, 20, 0, 10, 757788), null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='hora',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 19, 20, 0, 10, 754701), help_text='Hora', max_length=20),
        ),
    ]
