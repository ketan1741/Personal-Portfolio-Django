# Generated by Django 4.0.6 on 2022-09-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_skill_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image_filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='image_filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='image_filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image_filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
