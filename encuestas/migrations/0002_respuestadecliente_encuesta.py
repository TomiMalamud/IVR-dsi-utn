# Generated by Django 4.2.1 on 2023-05-29 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestadecliente',
            name='encuesta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='respuestaDeCliente', to='encuestas.encuesta'),
        ),
    ]