# Generated by Django 3.2 on 2021-04-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedl', '0008_alter_movie_poster_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
