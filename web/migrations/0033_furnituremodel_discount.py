# Generated by Django 4.1.7 on 2023-03-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_alter_furnituremodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='furnituremodel',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='discount'),
        ),
    ]