# Generated by Django 3.2.5 on 2021-07-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_app', '0012_pagecontrolpanel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagecontrolpanel',
            options={'verbose_name': 'Page Control Panel', 'verbose_name_plural': 'Page Control Panel'},
        ),
        migrations.AddField(
            model_name='pagecontrolpanel',
            name='name',
            field=models.CharField(default='', help_text='Enter the name of the panel', max_length=255, verbose_name='Name of Panel'),
            preserve_default=False,
        ),
    ]