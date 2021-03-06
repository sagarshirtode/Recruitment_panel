# Generated by Django 3.0.3 on 2020-05-19 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_details',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
                ('c_password', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'admin_details',
            },
        ),
        migrations.CreateModel(
            name='analysis_point',
            fields=[
                ('j_id', models.IntegerField(primary_key=True, serialize=False)),
                ('communication', models.IntegerField()),
                ('personality', models.IntegerField()),
                ('mentalability', models.IntegerField()),
                ('integrity', models.IntegerField()),
                ('job_knowledge', models.IntegerField()),
                ('situational_judgement', models.IntegerField()),
                ('t_analysis_point', models.IntegerField()),
            ],
            options={
                'db_table': 'analysis_point',
            },
        ),
        migrations.CreateModel(
            name='document_details',
            fields=[
                ('j_id', models.IntegerField(primary_key=True, serialize=False)),
                ('aadhar', models.URLField()),
                ('photo', models.URLField()),
                ('signature', models.URLField()),
                ('resume', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ischedule',
            fields=[
                ('post', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('iDate', models.DateField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
            options={
                'db_table': 'ischedule',
            },
        ),
        migrations.CreateModel(
            name='jobseeker_a_details',
            fields=[
                ('j_id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=10)),
                ('degree', models.CharField(max_length=15)),
                ('university', models.CharField(max_length=30)),
                ('institute', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=15)),
                ('semester', models.CharField(max_length=10)),
                ('cpi', models.CharField(max_length=5)),
                ('experience', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'jobseeker_a_details',
            },
        ),
        migrations.CreateModel(
            name='jobseeker_p_details',
            fields=[
                ('j_id', models.IntegerField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('contact', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=5)),
                ('birth_date', models.DateField()),
                ('state', models.CharField(max_length=15)),
                ('distric', models.CharField(max_length=15)),
                ('tahashil', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('pin', models.CharField(max_length=7)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'jobseeker_p_details',
            },
        ),
        migrations.CreateModel(
            name='jobseeker_registration',
            fields=[
                ('userName', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('c_password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'jobseeker_registration',
            },
        ),
        migrations.CreateModel(
            name='progress_report',
            fields=[
                ('j_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
                ('n_date', models.DateField()),
            ],
            options={
                'db_table': 'progress_report',
            },
        ),
        migrations.CreateModel(
            name='recruit_experience',
            fields=[
                ('j_id', models.IntegerField(primary_key=True, serialize=False)),
                ('month_of_experience', models.IntegerField()),
                ('company', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=30)),
                ('job_leaving_reason', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='requirement_statistics',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('post_name', models.CharField(max_length=20)),
                ('vacancies', models.IntegerField()),
                ('post_description', models.CharField(max_length=20)),
                ('min_salary', models.IntegerField()),
                ('max_salary', models.IntegerField()),
                ('qualification', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'requirement_statistics',
            },
        ),
        migrations.CreateModel(
            name='training_table',
            fields=[
                ('j_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_of_training', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('training_period', models.IntegerField()),
                ('start_training', models.DateField()),
                ('end_training', models.DateField()),
                ('t_analysis_point', models.IntegerField()),
                ('feedback', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'training_table',
            },
        ),
        migrations.CreateModel(
            name='application_hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('post_id', models.IntegerField()),
                ('post_name', models.CharField(max_length=40)),
                ('application_date', models.DateField()),
                ('j_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recruit.jobseeker_p_details')),
            ],
            options={
                'db_table': 'application_hit',
            },
        ),
    ]
