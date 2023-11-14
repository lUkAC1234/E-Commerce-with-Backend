# Generated by Django 4.1.7 on 2023-03-22 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_alter_contactusmodel_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furnituremodel',
            name='image',
            field=models.ImageField(upload_to='blogs/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='furnituremodel',
            name='price',
            field=models.PositiveBigIntegerField(verbose_name='price'),
        ),
    ]
