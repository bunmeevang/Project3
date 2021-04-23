# Generated by Django 3.2 on 2021-04-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codrs', '0003_auto_20210422_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('aboutme', models.CharField(max_length=500)),
                ('linkedin', models.CharField(max_length=100)),
            ],
        ),
    ]