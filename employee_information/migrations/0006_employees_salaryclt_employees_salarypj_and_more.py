# Generated by Django 5.0.7 on 2024-07-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0005_auto_20220302_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='salaryCLT',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='salaryPJ',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='salaryPS',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='salaryVA',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='salaryVR',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='salaryVT',
            field=models.FloatField(default=0),
        ),
    ]
