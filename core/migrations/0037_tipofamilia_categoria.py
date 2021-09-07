# Generated by Django 3.1.2 on 2021-06-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_tipofamilia'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipofamilia',
            name='categoria',
            field=models.CharField(choices=[('Herramientas', 'Herramienta'), ('Indumentarias', 'Indumentaria'), ('Iluminación', 'Iluminación_Y_Redes'), ('Materiales', 'Material'), ('Maderas', 'Madera')], default='Herramientas', max_length=20),
            preserve_default=False,
        ),
    ]
