# Generated by Django 4.1.7 on 2023-05-09 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0003_coursemapping_course_staff_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='staff_ID',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='courses',
        ),
        migrations.DeleteModel(
            name='CourseMapping',
        ),
    ]
