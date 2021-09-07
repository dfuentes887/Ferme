# Generated by Django 3.1.2 on 2021-06-23 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210514_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='csvs')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='herramienta',
        ),
        migrations.AddField(
            model_name='marca',
            name='codigo',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Herramienta', 'Herramienta'), ('Indumentaria', 'Indumentaria'), ('Iluminación', 'Iluminación_Y_Redes'), ('Material', 'Material'), ('Madera', 'Madera')], default='OWO', max_length=20),
            preserve_default=False,
        ),
    ]
