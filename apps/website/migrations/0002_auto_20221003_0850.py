# Generated by Django 3.2 on 2022-10-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='management',
            options={'verbose_name_plural': 'Management'},
        ),
        migrations.AddField(
            model_name='management',
            name='name',
            field=models.CharField(default='name', max_length=512),
        ),
    ]
