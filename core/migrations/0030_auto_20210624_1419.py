# Generated by Django 3.1.2 on 2021-06-24 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_tipoproducto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoproducto',
            name='Nombre',
        ),
        migrations.AddField(
            model_name='tipoproducto',
            name='nombre',
            field=models.CharField(default='Madera', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='SKU',
            field=models.PositiveIntegerField(),
        ),
    ]
