# Generated by Django 4.0.6 on 2022-08-29 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_testimonial_end_year_testimonial_start_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='quote',
            new_name='major',
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='role',
            new_name='program',
        ),
    ]