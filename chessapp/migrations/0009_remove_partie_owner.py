# Generated by Django 4.1.2 on 2022-10-08 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chessapp', '0008_alter_partie_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partie',
            name='owner',
        ),
    ]