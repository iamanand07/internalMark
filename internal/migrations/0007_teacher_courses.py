# Generated by Django 4.1.7 on 2023-05-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0006_remove_teacher_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(to='internal.course'),
        ),
    ]