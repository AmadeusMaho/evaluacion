# Generated by Django 5.0.6 on 2024-06-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgjuegos',
            name='idImg',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
