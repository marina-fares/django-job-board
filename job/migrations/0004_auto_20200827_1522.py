# Generated by Django 3.1 on 2020-08-27 15:22

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]