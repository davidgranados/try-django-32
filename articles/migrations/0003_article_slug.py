# Generated by Django 3.2.21 on 2023-09-11 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20230910_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
