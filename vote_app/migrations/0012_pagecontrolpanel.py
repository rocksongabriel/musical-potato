# Generated by Django 3.2.5 on 2021-07-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_app', '0011_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageControlPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_voting_page', models.BooleanField(help_text='Tick this button if you want people to be able to visit the voting page to vote', verbose_name='Enable Voting Page')),
                ('enable_results_page', models.BooleanField(help_text='Tick this box if you want people to be able to view the election results page', verbose_name='Enable Results Page')),
            ],
            options={
                'verbose_name': 'Page Control Panel',
                'verbose_name_plural': 'Page Control Panels',
            },
        ),
    ]
