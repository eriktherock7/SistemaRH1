# Generated by Django 5.0.7 on 2024-09-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0006_employees_salaryclt_employees_salarypj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='gestorcliente',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='gestorextractta',
            field=models.TextField(blank=True, null=True),
        ),
    ]
