# Generated by Django 4.0.6 on 2022-08-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='doi_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='research_gate_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
