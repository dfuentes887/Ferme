# Generated by Django 3.1.2 on 2021-05-11 01:37

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_order_direccion_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccionfactura',
            name='telefono',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='direccionfactura',
            name='pais',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]