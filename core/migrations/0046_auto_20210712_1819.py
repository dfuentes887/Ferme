# Generated by Django 3.1.2 on 2021-07-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_producto_fechavenc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fechaVenc',
            field=models.DateField(blank=True, null=True),
        ),
    ]
