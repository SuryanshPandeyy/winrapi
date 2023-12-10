# Generated by Django 3.2.12 on 2023-10-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_dntelegram_isauthorized'),
    ]

    operations = [
        migrations.AddField(
            model_name='dntelegram',
            name='api_hash',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dntelegram',
            name='api_id',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dntelegram',
            name='phone',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]