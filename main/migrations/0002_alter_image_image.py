# Generated by Django 4.0 on 2024-02-01 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_contenttype_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
