# Generated by Django 3.1.7 on 2023-06-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0026_auto_20230612_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='feedback',
            field=models.BooleanField(null=True),
        ),
    ]
