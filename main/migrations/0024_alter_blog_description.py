# Generated by Django 4.0.6 on 2022-08-26 19:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]