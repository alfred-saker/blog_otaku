# Generated by Django 4.2.3 on 2023-07-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sous_content',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]