# Generated by Django 3.1.2 on 2021-06-24 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_producto_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoproducto',
            name='SKU',
        ),
    ]
