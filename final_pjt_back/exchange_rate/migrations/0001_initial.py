# Generated by Django 4.2.7 on 2023-11-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('cur_unit', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ttb', models.CharField(max_length=50)),
                ('tts', models.CharField(max_length=50)),
                ('deal_bas_r', models.CharField(max_length=50)),
                ('bkpr', models.CharField(max_length=50)),
                ('yy_efee_r', models.CharField(max_length=50)),
                ('ten_dd_efee_r', models.CharField(max_length=50)),
                ('kftc_bkpr', models.CharField(max_length=50)),
                ('kftc_deal_bas_r', models.CharField(max_length=50)),
                ('cur_nm', models.CharField(max_length=50)),
            ],
        ),
    ]