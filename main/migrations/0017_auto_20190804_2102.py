# Generated by Django 2.2.2 on 2019-08-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_teammember_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='username',
        ),
        migrations.AddField(
            model_name='teammember',
            name='user_name',
            field=models.CharField(blank=True, default='UserName', max_length=200),
        ),
    ]
