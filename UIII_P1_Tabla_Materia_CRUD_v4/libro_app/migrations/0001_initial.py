# Generated by Django 5.1 on 2024-11-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('Id_libro', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=200)),
                ('Autor', models.CharField(max_length=150)),
                ('Ilustrador', models.CharField(max_length=150)),
                ('Asalida', models.DateField()),
                ('Precio', models.FloatField()),
                ('Stock', models.IntegerField()),
            ],
        ),
    ]
