# Generated by Django 4.1.4 on 2023-01-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]
