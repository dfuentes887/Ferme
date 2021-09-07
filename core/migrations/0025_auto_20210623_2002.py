# Generated by Django 3.1.2 on 2021-06-24 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_producto_idmod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('HER', 'Herramienta'), ('IND', 'Indumentaria'), ('ILU', 'Iluminación_Y_Redes'), ('MAT', 'Material'), ('MAD', 'Madera')], max_length=20),
        ),
    ]
