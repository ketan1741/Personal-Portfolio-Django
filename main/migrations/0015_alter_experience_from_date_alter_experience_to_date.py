# Generated by Django 4.0.6 on 2022-08-26 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_userprofile_experiences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]