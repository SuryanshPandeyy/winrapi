# Generated by Django 3.2.12 on 2023-10-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20231026_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='DnSubscribe',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=1000)),
                ('type', models.CharField(max_length=1000)),
                ('amount', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'dn_subscribe',
            },
        ),
    ]