# Generated by Django 3.1.7 on 2023-06-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0025_services_confirm_working'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='services',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
