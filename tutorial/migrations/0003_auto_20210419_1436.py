# Generated by Django 3.1.7 on 2021-04-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_auto_20210418_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nextpost',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='previouspost',
            field=models.URLField(blank=True),
        ),
    ]