# Generated by Django 4.2.1 on 2023-05-29 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='blockId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rooms.block', verbose_name='Bloco'),
        ),
    ]
