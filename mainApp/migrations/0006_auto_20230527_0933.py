# Generated by Django 3.1.7 on 2023-05-27 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_auto_20230526_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_register',
            name='certificate_img',
            field=models.FileField(upload_to='static\\img\\certificate_img', verbose_name='Trade Certificate'),
        ),
        migrations.AlterField(
            model_name='emp_register',
            name='e_img',
            field=models.FileField(upload_to='static\\img\\emp_img', verbose_name='Employee Image'),
        ),
    ]
