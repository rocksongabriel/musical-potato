# Generated by Django 3.2.5 on 2021-07-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_app', '0008_auto_20210708_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='picture',
            field=models.ImageField(help_text='Upload the image of the candidate', upload_to='media/candidates/pictures/', verbose_name='Picture of Candidate'),
        ),
    ]