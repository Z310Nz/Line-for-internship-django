# Generated by Django 5.0 on 2024-01-10 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_job_jobdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
