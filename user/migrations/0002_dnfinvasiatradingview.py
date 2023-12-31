# Generated by Django 3.2.12 on 2023-10-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DnFinvasiaTradingView',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=1000)),
                ('symbol', models.CharField(max_length=1000)),
                ('exchange', models.CharField(max_length=1000)),
                ('strike_price', models.CharField(max_length=1000)),
                ('quantity', models.CharField(max_length=1000)),
                ('expiry', models.CharField(max_length=1000)),
                ('delivery', models.CharField(max_length=1000)),
                ('market_type', models.CharField(max_length=1000)),
                ('edge_size', models.CharField(max_length=1000)),
                ('target', models.CharField(max_length=1000)),
                ('stoploss', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'dn_finvasia_trading_view',
            },
        ),
    ]
