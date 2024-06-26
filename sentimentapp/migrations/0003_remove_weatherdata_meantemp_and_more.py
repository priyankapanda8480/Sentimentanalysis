# Generated by Django 4.2.3 on 2024-06-10 13:54

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentapp', '0002_alter_sentimentanalysis_sentiment_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='meantemp',
        ),
        migrations.AddField(
            model_name='sentimentanalysis',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 6, 10, 13, 47, 7, 956316, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='weather_data',
            field=models.CharField(default=datetime.datetime(2024, 6, 10, 13, 54, 34, 205171, tzinfo=datetime.timezone.utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sentimentanalysis',
            name='sentiment_data',
            field=models.CharField(max_length=255),
        ),
    ]
