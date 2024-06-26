# Generated by Django 3.2.5 on 2021-07-19 21:05

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_voted'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateAccountAndMailStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(help_text='Enter name of batch you are uploading. eg. First Batch', max_length=100, verbose_name='Name of Batch')),
                ('csv', models.FileField(help_text='Upload the CSV file to create the accounts', upload_to='accounts/csv/', verbose_name='CSV File')),
            ],
            options={
                'verbose_name': 'Create Account and Mail Student',
            },
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
    ]
