# Generated by Django 4.2.3 on 2024-06-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentapp', '0003_remove_weatherdata_meantemp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
