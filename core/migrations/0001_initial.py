# Generated by Django 3.1.2 on 2021-04-02 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=15, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.comuna')),
            ],
        ),
    ]