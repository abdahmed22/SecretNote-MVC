# Generated by Django 5.0.7 on 2024-07-17 14:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_remove_note_id_note_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='destruction_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]