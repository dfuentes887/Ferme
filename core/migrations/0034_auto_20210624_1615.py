# Generated by Django 3.1.2 on 2021-06-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_tipoproducto_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoproducto',
            name='SKU',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]