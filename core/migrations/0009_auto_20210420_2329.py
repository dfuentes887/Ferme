# Generated by Django 3.1.2 on 2021-04-21 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210420_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='producto',
            new_name='productos',
        ),
    ]
