# Generated by Django 5.0.6 on 2024-05-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_songs_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='songs',
            index=models.Index(fields=['id'], name='music_songs_id_8977f4_idx'),
        ),
    ]
