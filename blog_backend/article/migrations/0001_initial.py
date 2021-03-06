# Generated by Django 3.1.3 on 2020-12-01 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('article_detail', models.TextField(max_length=200)),
                ('article_name', models.CharField(max_length=150)),
                ('article_content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('time_published', models.DateField(auto_now=True)),
                ('views', models.IntegerField(default=0, null=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to='article.UserSession')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor_name', models.CharField(max_length=100, null=True)),
                ('comment', models.TextField()),
                ('comment_on', models.DateTimeField(auto_now_add=True)),
                ('commented_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.posts')),
                ('unique_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ID', to='article.usersession')),
            ],
        ),
    ]
