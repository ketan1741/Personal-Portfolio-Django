# Generated by Django 4.0.6 on 2022-08-26 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_experience_from_date_alter_experience_to_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='from_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
