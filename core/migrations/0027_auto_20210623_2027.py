# Generated by Django 3.1.2 on 2021-06-24 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20210623_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Herramientas', 'Herramienta'), ('Indumentarias', 'Indumentaria'), ('Iluminación', 'Iluminación_Y_Redes'), ('Materiales', 'Material'), ('Maderas', 'Madera')], max_length=20),
        ),
    ]
