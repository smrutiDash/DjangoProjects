# Generated by Django 3.1.1 on 2020-12-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0003_apply_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_job',
            name='Mobile_no',
            field=models.CharField(max_length=100),
        ),
    ]
