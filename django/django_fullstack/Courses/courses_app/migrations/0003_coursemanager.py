# Generated by Django 5.0.6 on 2024-06-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_rename_descriptipn_course_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
