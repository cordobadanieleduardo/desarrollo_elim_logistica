# Generated by Django 5.1.6 on 2025-03-01 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0019_gastoconductor_vehiculo_alter_gastoconductor_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastoconductor',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 28, 23, 27, 37, 520874), null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 28, 23, 27, 37, 518888), null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='hora',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 28, 23, 27, 37, 512806), max_length=20),
        ),
    ]
