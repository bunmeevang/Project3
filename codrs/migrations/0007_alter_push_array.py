# Generated by Django 3.2 on 2021-04-25 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codrs', '0006_auto_20210424_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='push',
            name='array',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pushes', to='codrs.array'),
        ),
    ]