# Generated by Django 5.0 on 2024-05-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_usersignup_profil_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='profil_img',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='profile_images/'),
        ),
    ]
