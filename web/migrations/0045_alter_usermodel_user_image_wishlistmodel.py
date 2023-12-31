# Generated by Django 4.1.7 on 2023-03-25 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0044_alter_contactusmodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_image',
            field=models.ImageField(default='users/avatar.png', upload_to='users/%y/%m/%d'),
        ),
        migrations.CreateModel(
            name='WishListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furniture', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='wishlist', to='web.furnituremodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='wishlistuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'wishlist',
                'verbose_name_plural': 'wishlists',
                'unique_together': {('user', 'furniture')},
            },
        ),
    ]
