# Generated by Django 5.0 on 2024-01-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cv',
            field=models.URLField(),
        ),
    ]
