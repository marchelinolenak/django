# Generated by Django 3.0.7 on 2020-06-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200612_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(default='www.google.com'),
        ),
    ]
