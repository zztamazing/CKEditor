# Generated by Django 4.1.5 on 2023-02-13 09:25

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passage',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文部分'),
        ),
    ]
