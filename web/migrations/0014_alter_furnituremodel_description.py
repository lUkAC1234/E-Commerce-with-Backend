# Generated by Django 4.1.7 on 2023-03-21 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_furnituremodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furnituremodel',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]