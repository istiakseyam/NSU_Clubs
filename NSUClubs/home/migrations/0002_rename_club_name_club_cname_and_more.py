# Generated by Django 4.0.2 on 2022-04-04 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='club_name',
            new_name='cname',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='club_sname',
            new_name='csname',
        ),
    ]
