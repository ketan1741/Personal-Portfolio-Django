# Generated by Django 4.0.6 on 2022-08-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_alter_contactprofile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='end_year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='start_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
