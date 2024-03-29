# Generated by Django 5.0.1 on 2024-02-22 16:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookauthor',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
