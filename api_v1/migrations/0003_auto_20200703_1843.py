# Generated by Django 3.0.5 on 2020-07-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_auto_20200703_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
