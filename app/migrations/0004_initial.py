# Generated by Django 5.0 on 2024-03-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_delete_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='usersignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('laststname', models.CharField(max_length=20)),
                ('gmail', models.EmailField(max_length=254)),
                ('pin', models.CharField(max_length=20)),
            ],
        ),
    ]
