# Generated by Django 4.1.7 on 2023-03-22 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_alter_furnituremodel_colors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactusmodel',
            name='message',
            field=models.CharField(max_length=300, null=True, verbose_name='message'),
        ),
    ]