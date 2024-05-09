# Generated by Django 5.0.4 on 2024-05-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ID_recuperation',
            field=models.IntegerField(verbose_name='Id de recuperacion'),
        ),
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateField(verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_bloqued',
            field=models.BooleanField(default=False, verbose_name='Bloquear'),
        ),
        migrations.AlterField(
            model_name='user',
            name='request_verification',
            field=models.BooleanField(default=False, verbose_name='Solicita verificacion'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.IntegerField(default=0, verbose_name='Tipo de usuario'),
        ),
    ]
