# Generated by Django 4.1.7 on 2023-03-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_colorsmodel_furnituremodel_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furnituremodel',
            name='colors',
            field=models.ManyToManyField(related_name='furnitureColors', to='web.colorsmodel', verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='furnituremodel',
            name='tags',
            field=models.ManyToManyField(related_name='furnitureTags', to='web.tagsmodel', verbose_name='tag'),
        ),
    ]
