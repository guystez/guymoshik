# Generated by Django 4.1.2 on 2022-10-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='street_number',
            field=models.SmallIntegerField(max_length=100),
        ),
    ]
