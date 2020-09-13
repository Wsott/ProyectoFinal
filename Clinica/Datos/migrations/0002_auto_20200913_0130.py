# Generated by Django 3.1.1 on 2020-09-13 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='fk_persona_dni',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Datos.persona'),
            preserve_default=False,
        ),
    ]