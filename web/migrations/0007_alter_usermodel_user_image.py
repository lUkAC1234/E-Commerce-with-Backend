# Generated by Django 4.1.7 on 2023-03-18 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_usermodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_image',
            field=models.ImageField(default='avatar.png', upload_to='users/'),
        ),
    ]
