# Generated by Django 3.1 on 2020-08-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20200827_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
