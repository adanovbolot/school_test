# Generated by Django 4.0.6 on 2022-07-31 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_remove_teacher_class_student_teacher_class_school_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_student',
            field=models.CharField(help_text='формат: 1-класс, группа-a, b, c', max_length=100, verbose_name='Класс'),
        ),
    ]
