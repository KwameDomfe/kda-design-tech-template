# Generated by Django 3.2 on 2022-10-24 10:36

import apps.website.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_management_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default='Give a brief description of Section here', max_length=512)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created', '-updated', 'name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='management',
            options={'ordering': ['description'], 'verbose_name_plural': 'Management'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name', '-start_date'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['id'], 'verbose_name_plural': 'Sub Categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='management',
            old_name='dateOfFirstAppointment',
            new_name='date_of_first_appointment',
        ),
        migrations.RenameField(
            model_name='management',
            old_name='position_id',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='management',
            old_name='staff_id',
            new_name='staff',
        ),
        migrations.RemoveField(
            model_name='management',
            name='name',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='project_id',
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.TextField(default='Give a brief description of Department here', max_length=512),
        ),
        migrations.AddField(
            model_name='management',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.department'),
        ),
        migrations.AddField(
            model_name='management',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.office'),
        ),
        migrations.AddField(
            model_name='projectdetail',
            name='project',
            field=models.OneToOneField(default='true', on_delete=django.db.models.deletion.CASCADE, parent_link=apps.website.models.Project, to='website.project'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_floor_area',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='projectlead',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.project'),
        ),
        migrations.AlterField(
            model_name='projectoverview',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.project'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='pub_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Date Published'),
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
        migrations.AddField(
            model_name='department',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.section'),
        ),
    ]
