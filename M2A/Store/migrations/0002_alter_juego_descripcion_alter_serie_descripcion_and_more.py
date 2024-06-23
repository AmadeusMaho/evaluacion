# Generated by Django 5.0.6 on 2024-06-22 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='descripcion',
            field=models.CharField(max_length=220),
        ),
        migrations.AlterField(
            model_name='serie',
            name='descripcion',
            field=models.CharField(max_length=220),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idCarro', models.IntegerField(primary_key=True, serialize=False)),
                ('idUsuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Store.usuario')),
                ('juegos', models.ManyToManyField(blank=True, related_name='carritos', to='Store.juego')),
                ('series', models.ManyToManyField(blank=True, related_name='carritos', to='Store.serie')),
            ],
        ),
    ]
