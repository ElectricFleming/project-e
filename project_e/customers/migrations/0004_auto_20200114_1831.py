# Generated by Django 2.2.7 on 2020-01-15 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_dealer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='dealer_id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='cust_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]