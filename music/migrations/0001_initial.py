# Generated by Django 4.2 on 2023-04-30 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.TextField()),
                ('artist', models.TextField()),
                ('duration', models.FloatField()),
                ('Audio_file', models.FileField(blank=True, null=True, upload_to='')),
                ('Audio_link', models.FileField(max_length=200, upload_to='')),
            ],
        ),
    ]
