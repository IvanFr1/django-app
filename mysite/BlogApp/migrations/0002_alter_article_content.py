# Generated by Django 5.0.3 on 2024-07-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
