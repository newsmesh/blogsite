# Generated by Django 4.0.2 on 2022-03-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20220212_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(unique=True),
        ),
    ]
