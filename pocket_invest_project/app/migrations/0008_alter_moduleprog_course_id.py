# Generated by Django 4.0.2 on 2022-02-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_moduleprog_delete_moduleprogress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleprog',
            name='course_id',
            field=models.IntegerField(),
        ),
    ]
