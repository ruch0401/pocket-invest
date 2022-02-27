# Generated by Django 4.0.2 on 2022-02-27 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_moduleprogress_course_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleProg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_count', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.DeleteModel(
            name='ModuleProgress',
        ),
    ]