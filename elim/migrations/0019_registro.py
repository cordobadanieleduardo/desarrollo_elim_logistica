# Generated by Django 5.1.5 on 2025-02-12 03:07

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0018_delete_registro'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('numero_registo', models.UUIDField(default=uuid.uuid4)),
                ('celular', models.CharField(max_length=10)),
                ('medio_pago', models.CharField(choices=[('CONTADO', 'Contado'), ('CREDITO', 'Crédito'), ('TRANSFERENCIA', 'Transferencia')], default='CONTADO', max_length=15)),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('costo', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('neto', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cliente', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='elim.cliente')),
                ('placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elim.vehiculo')),
                ('programador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elim.programador')),
                ('solicitado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elim.persona')),
                ('trayecto', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='elim.trayecto')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Registros',
            },
        ),
    ]
