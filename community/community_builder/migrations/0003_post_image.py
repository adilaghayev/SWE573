# Generated by Django 2.2.7 on 2019-12-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_builder', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
