# Generated by Django 2.1.5 on 2019-01-30 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmgmt', '0008_auto_20190129_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profilepic',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='booksissued',
            name='issuedate',
            field=models.DateField(default=datetime.date(2019, 1, 30)),
        ),
    ]