# Generated by Django 4.1.7 on 2023-03-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0033_furnituremodel_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorsmodel',
            name='name',
            field=models.CharField(max_length=7, verbose_name='name'),
        ),
    ]