# Generated by Django 3.2 on 2021-05-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click on the button below to read about this blog post...', max_length=60),
        ),
    ]