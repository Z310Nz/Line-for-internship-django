# Generated by Django 5.0 on 2024-01-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logoc', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('company_name', models.CharField(max_length=255)),
                ('foundation_date', models.DateField()),
                ('company_type', models.CharField(max_length=255)),
                ('number_of_employees', models.IntegerField()),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('address_label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jobdetail', models.CharField(max_length=255)),
                ('workplace', models.CharField(max_length=255)),
                ('worktype', models.CharField(max_length=255)),
                ('quality', models.CharField(max_length=255)),
                ('benefit', models.CharField(max_length=255)),
                ('workstart', models.TimeField()),
                ('workend', models.TimeField()),
                ('workday', models.CharField(max_length=255)),
            ],
        ),
    ]
