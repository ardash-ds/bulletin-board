# Generated by Django 3.2.9 on 2021-12-14 12:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_answer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
