# Generated by Django 5.1.5 on 2025-02-08 16:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elim', '0004_alter_servicio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
    ]
