# Generated by Django 3.1.1 on 2020-09-23 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0010_auto_20200923_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='fk_persona_dni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Datos.persona'),
        ),
    ]
