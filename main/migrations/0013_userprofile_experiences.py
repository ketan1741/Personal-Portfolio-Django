# Generated by Django 4.0.6 on 2022-08-25 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_date_experience_from_date_experience_to_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='experiences',
            field=models.ManyToManyField(blank=True, to='main.experience'),
        ),
    ]
