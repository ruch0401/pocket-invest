# Generated by Django 4.0.2 on 2022-02-27 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_moduleprogress_completion_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moduleprogress',
            old_name='course_id',
            new_name='course_name',
        ),
    ]