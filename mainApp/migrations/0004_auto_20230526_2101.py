# Generated by Django 3.1.7 on 2023-05-26 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20230526_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp_register',
            old_name='on_duty',
            new_name='available',
        ),
    ]