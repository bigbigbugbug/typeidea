# Generated by Django 3.0 on 2019-12-16 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20191216_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='website',
            new_name='email',
        ),
    ]