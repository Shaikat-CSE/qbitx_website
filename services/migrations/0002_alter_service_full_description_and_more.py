# Generated by Django 5.2 on 2025-04-13 06:31

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='full_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='servicefaq',
            name='answer',
            field=tinymce.models.HTMLField(),
        ),
    ]
