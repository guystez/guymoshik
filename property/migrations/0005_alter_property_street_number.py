# Generated by Django 4.1.2 on 2022-10-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0004_alter_property_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="street_number",
            field=models.SmallIntegerField(verbose_name="street_number"),
        ),
    ]