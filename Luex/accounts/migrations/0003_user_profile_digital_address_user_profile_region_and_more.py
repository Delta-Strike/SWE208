# Generated by Django 4.1.13 on 2024-08-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_phone_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='Digital_address',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='Region',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='address',
            field=models.CharField(default='', max_length=20),
        ),
    ]
