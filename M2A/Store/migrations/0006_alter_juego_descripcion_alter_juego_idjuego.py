# Generated by Django 5.0.6 on 2024-06-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_alter_carrito_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='descripcion',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='juego',
            name='idJuego',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
