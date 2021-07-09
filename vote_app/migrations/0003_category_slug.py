# Generated by Django 3.2.5 on 2021-07-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_app', '0002_alter_candidate_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', help_text='Slug of the category', unique=True, verbose_name='Slug'),
        ),
    ]
