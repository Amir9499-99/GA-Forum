# Generated by Django 3.0.2 on 2020-03-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reply',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
    ]