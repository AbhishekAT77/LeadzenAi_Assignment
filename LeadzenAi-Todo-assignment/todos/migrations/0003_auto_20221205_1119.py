# Generated by Django 3.0.4 on 2022-12-05 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20210219_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-date_created']},
        ),
    ]
