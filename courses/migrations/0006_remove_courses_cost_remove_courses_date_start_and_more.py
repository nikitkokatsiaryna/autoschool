# Generated by Django 4.2 on 2023-05-09 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_courses_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='date_start',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='description',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='name',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='spaces_remaining',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='type_program',
        ),
    ]