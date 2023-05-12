# Generated by Django 4.1.7 on 2023-05-09 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0004_remove_course_staff_id_remove_teacher_courses_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='internal.course'),
            preserve_default=False,
        ),
    ]