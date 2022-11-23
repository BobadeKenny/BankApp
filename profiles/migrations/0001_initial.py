# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50, default=None)),
                ('sex', models.CharField(max_length=1, default=None)),
                ('annual_income', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, default=None)),
                ('mobile', models.IntegerField(default=0)),
                ('occupation', models.CharField(max_length=50, default=None)),
                ('DOB', models.DateField(default=None)),
                ('user_name', models.CharField(max_length=150, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyTransfer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('enter_your_user_name', models.CharField(max_length=150, default=None)),
                ('enter_the_destination_account_number', models.IntegerField()),
                ('enter_the_amount_to_be_transferred_in_NGN', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PresentLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('country', models.CharField(max_length=50, default='India')),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('user_name', models.CharField(max_length=150, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('account_number', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('user_name', models.CharField(max_length=150, default=None)),
            ],
        ),
    ]
