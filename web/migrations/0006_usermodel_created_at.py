# Generated by Django 4.1.7 on 2023-03-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_usermodel_github_username_usermodel_twitter_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
