# Generated by Django 4.2.3 on 2023-07-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_genre_tag_remove_article_tag_article_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ManyToManyField(to='articles.categorie'),
        ),
    ]