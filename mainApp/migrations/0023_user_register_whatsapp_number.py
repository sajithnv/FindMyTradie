# Generated by Django 3.1.7 on 2023-06-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0022_auto_20230609_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_register',
            name='whatsapp_number',
            field=models.CharField(default='0', max_length=10, verbose_name='Whatsapp_Number'),
        ),
    ]