# Generated by Django 3.1.2 on 2021-06-24 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20210624_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.tipoproducto'),
            preserve_default=False,
        ),
    ]
