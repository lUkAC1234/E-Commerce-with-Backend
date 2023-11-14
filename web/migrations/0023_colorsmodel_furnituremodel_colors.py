# Generated by Django 4.1.7 on 2023-03-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_tagsmodel_furnituremodel_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.AddField(
            model_name='furnituremodel',
            name='colors',
            field=models.ManyToManyField(related_name='furniture', to='web.colorsmodel', verbose_name='tag'),
        ),
    ]