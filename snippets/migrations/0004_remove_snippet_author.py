# Generated by Django 4.1.2 on 2022-10-09 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_alter_author_country_alter_author_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='author',
        ),
    ]
