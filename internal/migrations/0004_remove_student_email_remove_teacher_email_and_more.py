# Generated by Django 4.1.7 on 2023-04-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0003_alter_user_is_admin_alter_user_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='Anand', max_length=50),
            preserve_default=False,
        ),
    ]
