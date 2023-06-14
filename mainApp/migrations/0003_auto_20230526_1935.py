# Generated by Django 3.1.7 on 2023-05-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_remove_user_register_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp_register',
            name='registered',
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='registered',
        ),
        migrations.AlterField(
            model_name='user_register',
            name='u_name',
            field=models.CharField(max_length=100, null=True, verbose_name='User_Name'),
        ),
    ]
