# Generated by Django 5.1.6 on 2025-04-03 12:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0014_alter_vehiculo_enfermo_alter_vehiculo_mecanico_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='cotizacion',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='factura',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro',
            name='legalizado',
            field=models.CharField(choices=[('Sin legalizar', 'Sin legalizar'), ('Legalizado', 'Legalizado')], default='Sin legalizar', max_length=15),
        ),
        migrations.AddField(
            model_name='registro',
            name='status',
            field=models.CharField(choices=[('creado', 'Creado'), ('ejecutado', 'Ejecutado'), ('cotizado', 'Cotizado'), ('facturado', 'Facturado'), ('no_show', 'NO SHOW')], default='creado', max_length=15),
        ),
    ]
