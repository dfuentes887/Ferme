# Generated by Django 3.1.2 on 2021-06-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_producto_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='categoria',
            field=models.CharField(choices=[('Herramientas', 'Herramienta'), ('Indumentarias', 'Indumentaria'), ('Iluminación', 'Iluminación_Y_Redes'), ('Materiales', 'Material'), ('Maderas', 'Madera')], default='Herramientas', max_length=20),
            preserve_default=False,
        ),
    ]
