# Generated by Django 3.0.7 on 2023-01-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230101_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(default='123 st', max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(default='AI', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.CharField(default='011', max_length=20),
        ),
    ]
