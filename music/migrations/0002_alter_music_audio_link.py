# Generated by Django 4.2 on 2023-04-30 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='Audio_link',
            field=models.FileField(blank=True, max_length=200, upload_to=''),
        ),
    ]
