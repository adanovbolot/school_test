# Generated by Django 4.0.6 on 2022-07-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Черновик'),
        ),
    ]
