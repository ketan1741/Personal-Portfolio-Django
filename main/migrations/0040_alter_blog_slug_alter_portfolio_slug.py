# Generated by Django 4.0.6 on 2022-09-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_userprofile_cv_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True),
        ),
    ]
