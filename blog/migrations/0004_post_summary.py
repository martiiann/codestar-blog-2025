# Generated by Django 5.1.7 on 2025-04-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
