# Generated by Django 5.0 on 2024-01-06 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RobotsAPI', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='robot',
            old_name='rob_model',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='robot',
            old_name='ver_robot',
            new_name='version',
        ),
    ]
