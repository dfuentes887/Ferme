# Generated by Django 3.1.2 on 2021-07-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_auto_20210712_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='correo',
            field=models.EmailField(default='formail@granidisco.com', max_length=254),
            preserve_default=False,
        ),
    ]
