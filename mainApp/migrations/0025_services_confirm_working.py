# Generated by Django 3.1.7 on 2023-06-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0024_auto_20230611_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='confirm_working',
            field=models.BooleanField(default=False),
        ),
    ]