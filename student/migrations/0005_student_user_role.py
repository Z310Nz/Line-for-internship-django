# Generated by Django 5.0 on 2024-01-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user_role',
            field=models.CharField(default='student', max_length=255),
        ),
    ]