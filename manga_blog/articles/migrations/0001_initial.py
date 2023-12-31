# Generated by Django 4.2.3 on 2023-07-23 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categorie', models.CharField(choices=[('Combat', 'Combat'), ('Aventure', 'Aventure'), ('Fantasy', 'Fantasy'), ('Action', 'Action'), ('Comedie', 'Comedie'), ('Surnaturel', 'Surnaturel'), ('Drame', 'Drame'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi')], max_length=200)),
                ('tag', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
