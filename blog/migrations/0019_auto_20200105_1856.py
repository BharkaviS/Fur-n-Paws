# Generated by Django 2.1.7 on 2020-01-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_blogpost_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='username',
            field=models.CharField(default=True, max_length=120, verbose_name='auth.User'),
        ),
    ]