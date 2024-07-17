# Generated by Django 5.0.7 on 2024-07-17 07:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='id',
        ),
        migrations.AddField(
            model_name='note',
            name='secret',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]