# Generated by Django 5.1.6 on 2025-02-19 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0040_alter_registro_fecha_alter_trayecto_zipcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 19, 18, 9, 7, 592051), null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='hora',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 19, 18, 9, 7, 588669), help_text='Hora', max_length=20),
        ),
    ]
