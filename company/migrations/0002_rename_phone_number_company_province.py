# Generated by Django 5.0 on 2024-01-10 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='phone_number',
            new_name='province',
        ),
    ]
