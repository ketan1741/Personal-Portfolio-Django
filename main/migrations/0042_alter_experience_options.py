# Generated by Django 4.0.6 on 2022-09-02 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_alter_experience_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['id'], 'verbose_name': 'Experience', 'verbose_name_plural': 'Experiences'},
        ),
    ]