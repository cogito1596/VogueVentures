# Generated by Django 3.1 on 2024-04-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=' ', unique=True),
        ),
    ]
