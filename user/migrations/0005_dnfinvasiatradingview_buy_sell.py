# Generated by Django 3.2.12 on 2023-10-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_dnfinvasiatradingview_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnfinvasiatradingview',
            name='buy_sell',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
