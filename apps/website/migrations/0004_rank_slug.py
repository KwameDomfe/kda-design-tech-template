# Generated by Django 3.2 on 2022-10-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20221003_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
