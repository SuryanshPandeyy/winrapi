# Generated by Django 3.2.12 on 2023-10-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_dnfinvasiatradingview_buy_sell'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnfinvasiausercredsmaster',
            name='unique_code',
            field=models.CharField(default='000000', max_length=1000),
            preserve_default=False,
        ),
    ]
