# Generated by Django 3.1.2 on 2021-04-21 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_producto_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='orderproducto',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]
