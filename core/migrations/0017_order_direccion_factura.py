# Generated by Django 3.1.2 on 2021-05-11 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_direccionfactura'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='direccion_factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.direccionfactura'),
        ),
    ]