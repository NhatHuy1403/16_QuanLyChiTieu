# Generated by Django 4.1.7 on 2023-04-22 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userincome', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userincome',
            options={'ordering': ['-date']},
        ),
    ]