# Generated by Django 5.1.6 on 2025-02-15 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0024_rename_city_trayecto_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='medio_pago',
            field=models.CharField(choices=[('CONTADO', 'Contado'), ('CREDITO', 'Crédito'), ('TRANSFERENCIA', 'Transferencia')], default='CONTADO', max_length=15, verbose_name='Medio de peago'),
        ),
    ]
