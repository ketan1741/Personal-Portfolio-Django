# Generated by Django 4.0.6 on 2022-08-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_ver_link_certificate_verification_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]