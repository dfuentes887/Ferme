# Generated by Django 3.1.2 on 2021-06-23 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20210623_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='idMod',
            field=models.CharField(default=12345699999999123, max_length=50),
            preserve_default=False,
        ),
    ]