# Generated by Django 3.1.1 on 2020-09-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0002_auto_20200913_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
