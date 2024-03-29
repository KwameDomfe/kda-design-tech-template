# Generated by Django 3.2 on 2023-05-10 19:34

import apps.website.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=512, null=True)),
                ('thumbnail', models.FileField(blank=True, upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Project Categories',
                'ordering': ['-created', '-updated', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default='Give a brief description of Department here', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': 'Gender',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=128, null=True, verbose_name='Surname')),
                ('lastname', models.CharField(max_length=128, null=True, verbose_name='Lastname')),
                ('othername', models.CharField(blank=True, max_length=128, verbose_name='Other Names')),
                ('description', models.TextField(max_length=512, verbose_name='Description')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('mobile_1', models.CharField(blank=True, max_length=14)),
                ('mobile_2', models.CharField(blank=True, max_length=14)),
                ('email', models.EmailField(blank=True, max_length=64)),
                ('alt_email', models.EmailField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default='type something here', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default='Give a brief description of Profession here', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(default='_images/placeholders/regular_images/square-01.png', upload_to='images/projects/')),
                ('location', models.CharField(max_length=128, null=True)),
                ('cost', models.CharField(default='', max_length=128, null=True)),
                ('client', models.CharField(max_length=128, null=True)),
                ('total_floor_area', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('jobsheet', models.FileField(blank=True, null=True, upload_to='')),
                ('start_date', models.DateField(auto_now_add=True, null=True)),
                ('completed_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['name', '-start_date'],
            },
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.OneToOneField(default='true', on_delete=django.db.models.deletion.CASCADE, parent_link=apps.website.models.Project, to='website.project')),
                ('title', models.CharField(max_length=256)),
                ('title_details', models.CharField(max_length=256)),
                ('created_date', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(default='type something here', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default='Give a brief description of Section here', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Sub Category Name')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(max_length=512, null=True, verbose_name='Sub Category Description')),
                ('thumbnail', models.FileField(blank=True, upload_to='')),
                ('pub_date', models.DateField(auto_now=True, null=True, verbose_name='Date Published')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.category')),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_number', models.CharField(default='QW23', max_length=32)),
                ('description', models.TextField(max_length=512)),
                ('dateOfFirstAppointment', models.DateField(blank=True, null=True, verbose_name='date of First Appointment')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.department')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.office')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.person')),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.profession')),
                ('rank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.rank')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default='Give a brief description of Services here', max_length=512)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.department')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectOverview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(default='Project Overview', max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=256)),
                ('media_content', models.FileField(upload_to='')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.CharField(max_length=128, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.project')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.staff')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='coordinator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.staff'),
        ),
        migrations.AddField(
            model_name='project',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.subcategory'),
        ),
        migrations.AddField(
            model_name='office',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.region'),
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(max_length=512)),
                ('date_of_first_appointment', models.DateField(blank=True, null=True, verbose_name='date of First Appointment')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.department')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.office')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.position')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.staff')),
            ],
            options={
                'verbose_name_plural': 'Management',
                'ordering': ['description'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.section'),
        ),
        migrations.CreateModel(
            name='BoardOfDirector',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=512)),
                ('dateOfFirstAppointment', models.DateField(blank=True, null=True, verbose_name='date of First Appointment')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.person')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.position')),
            ],
        ),
    ]
