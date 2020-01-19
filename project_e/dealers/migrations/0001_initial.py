# Generated by Django 2.2.7 on 2020-01-19 02:44

from django.db import migrations, models
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('ref_id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=500, verbose_name='Address')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
        ),
    ]
