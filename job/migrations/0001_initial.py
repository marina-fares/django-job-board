# Generated by Django 3.1 on 2020-08-26 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=15)),
                ('descrpition', models.TextField(max_length=1000)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('vacancy', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=1)),
            ],
        ),
    ]
