# Generated by Django 4.2.1 on 2023-05-24 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefinale', '0003_employe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employe',
            old_name='id',
            new_name='matricule',
        ),
    ]
