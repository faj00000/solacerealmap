# Generated by Django 4.2.4 on 2023-08-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venttable',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
