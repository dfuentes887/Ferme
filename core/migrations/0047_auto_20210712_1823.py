# Generated by Django 3.1.2 on 2021-07-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_auto_20210712_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fechaVenc',
            field=models.DateField(blank=True, default='2020-06-02'),
            preserve_default=False,
        ),
    ]
