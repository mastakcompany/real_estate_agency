# Generated by Django 2.2.24 on 2023-08-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230807_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, null=True, verbose_name='Новое-ли здание?'),
        ),
    ]
