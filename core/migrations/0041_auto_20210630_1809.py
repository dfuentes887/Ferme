# Generated by Django 3.1.2 on 2021-06-30 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='rubro',
            field=models.CharField(max_length=255),
        ),
    ]