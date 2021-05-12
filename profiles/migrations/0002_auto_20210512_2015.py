# Generated by Django 3.2 on 2021-05-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='Write a brief about yourself here...'),
        ),
    ]
