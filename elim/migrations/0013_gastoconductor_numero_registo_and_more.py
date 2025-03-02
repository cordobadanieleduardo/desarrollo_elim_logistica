# Generated by Django 5.1.6 on 2025-02-28 22:18

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0012_alter_gastoconductor_fecha_alter_registro_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gastoconductor',
            name='numero_registo',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='gastoconductor',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 28, 17, 18, 20, 696441), null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 28, 17, 18, 20, 692899), null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='hora',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 28, 17, 18, 20, 687883), max_length=20),
        ),
    ]
