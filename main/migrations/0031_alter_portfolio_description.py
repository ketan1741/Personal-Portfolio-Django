# Generated by Django 4.0.6 on 2022-08-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_portfolio_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
