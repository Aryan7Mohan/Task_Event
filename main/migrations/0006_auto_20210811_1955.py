# Generated by Django 3.1.1 on 2021-08-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210811_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='time',
            field=models.DateTimeField(blank=True),
        ),
    ]