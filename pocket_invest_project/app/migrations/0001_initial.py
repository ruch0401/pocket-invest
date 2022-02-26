from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100)),
                ('article_content', models.TextField()),
                ('article_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('topic', models.CharField(max_length=100)),
                ('age_group', models.CharField(max_length=10)),
                ('total_modules', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_name', models.CharField(max_length=100)),
                ('investment_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_risk', models.CharField(max_length=100)),
                ('investment_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=100)),
                ('video_url', models.CharField(max_length=200)),
                ('module_content', models.TextField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email_id', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('random_id', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('real_money_balance', models.IntegerField(blank=True, null=True)),
                ('virtual_money_balance', models.IntegerField(blank=True, null=True)),
                ('user_type', models.IntegerField(blank=True, null=True)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('vendor_category', models.CharField(blank=True, max_length=100, null=True)),
                ('vendor_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('details', models.TextField()),
                ('outcome', models.CharField(max_length=20)),
                ('type_of_transaction', models.IntegerField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver2sender', to='app.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender2receiver', to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random_id', models.CharField(blank=True, max_length=100, null=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child2parent', to='app.user')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent2child', to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=100)),
                ('text_field', models.CharField(max_length=100)),
                ('completion_status', models.BooleanField()),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.module')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_amount', models.IntegerField()),
                ('investment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.investment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion_status', models.BooleanField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.module')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.AddField(
            model_name='investment',
            name='investment_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.investmentcategory'),
        ),
        migrations.CreateModel(
            name='CourseProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modules_completed', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
