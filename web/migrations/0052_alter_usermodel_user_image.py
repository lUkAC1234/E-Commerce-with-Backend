# Generated by Django 4.1.2 on 2023-03-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0051_alter_usermodel_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_image',
            field=models.ImageField(default='users/userDefaultImage.png', upload_to='users/%Y/%m/%d/', verbose_name='user image'),
        ),
    ]