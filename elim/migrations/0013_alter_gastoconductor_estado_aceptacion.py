# Generated by Django 5.1.6 on 2025-03-15 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0012_gastoconductor_credito_gastoconductor_efectivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastoconductor',
            name='estado_aceptacion',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
