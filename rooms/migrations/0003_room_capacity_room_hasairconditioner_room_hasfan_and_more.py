# Generated by Django 4.2.1 on 2023-05-31 00:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_room_blockid'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(default=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='room',
            name='hasAirConditioner',
            field=models.BooleanField(default=True, verbose_name='Ar Condicionado'),
        ),
        migrations.AddField(
            model_name='room',
            name='hasFan',
            field=models.BooleanField(default=True, verbose_name='Ventilador'),
        ),
        migrations.AddField(
            model_name='room',
            name='hasProjector',
            field=models.BooleanField(default=True, verbose_name='Projetor'),
        ),
        migrations.AddField(
            model_name='room',
            name='isAcessible',
            field=models.BooleanField(default=True, verbose_name='Acessibilidade'),
        ),
    ]
