# Generated by Django 4.2.3 on 2023-08-07 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_user', '0003_alter_userprofile_adresse_domicile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='adresse_domicile',
        ),
    ]