# Generated by Django 5.0.4 on 2024-05-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tries_left",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Intentos restantes"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="creation_date",
            field=models.DateField(auto_now_add=True, verbose_name="Fecha de registro"),
        ),
    ]
