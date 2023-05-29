# Generated by Django 4.2.1 on 2023-05-29 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Primeiro nomme')),
                ('last_name', models.CharField(max_length=25, verbose_name='Último nome')),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.course', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Professor(a)',
                'verbose_name_plural': 'Professores(as)',
            },
        ),
    ]
