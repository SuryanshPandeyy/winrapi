# Generated by Django 3.2.12 on 2023-10-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_dnfinvasiausercredsmaster_unique_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='DnTelegram',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=1000)),
                ('code', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'dn_telegram',
            },
        ),
    ]
