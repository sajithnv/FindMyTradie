# Generated by Django 3.1.7 on 2023-06-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0027_services_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
    ]
