# Generated by Django 3.0.5 on 2020-05-03 07:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default=datetime.datetime(2020, 5, 3, 7, 45, 2, 119426, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
