# Generated by Django 3.2.5 on 2021-09-03 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('videos', '0009_auto_20210903_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2)),
                ('publish_timestamp', models.DateTimeField(blank=True, null=True)),
                ('video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='videos.video')),
            ],
        ),
    ]