# Generated by Django 3.2.5 on 2021-07-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_app', '0013_auto_20210715_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
