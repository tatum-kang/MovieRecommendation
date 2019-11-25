# Generated by Django 2.2.7 on 2019-11-25 10:52

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
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieCd', models.IntegerField()),
                ('title', models.CharField(max_length=150)),
                ('title_en', models.CharField(max_length=150)),
                ('summary', models.TextField()),
                ('director', models.CharField(max_length=50)),
                ('poster_url', models.TextField()),
                ('trailer_url', models.TextField()),
                ('opendt', models.DateTimeField()),
                ('naver_score', models.FloatField()),
                ('grade', models.CharField(max_length=50)),
                ('avr_score', models.IntegerField(default=0)),
                ('actors', models.ManyToManyField(related_name='actors_movies', to='api.Actor')),
                ('genres', models.ManyToManyField(related_name='genres_movies', to='api.Genre')),
                ('liked_users', models.ManyToManyField(related_name='liked_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='api.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
