# Generated by Django 2.2.14 on 2021-07-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=50)),
                ('buyer_item', models.CharField(max_length=50)),
                ('buyer_cost', models.CharField(max_length=50)),
                ('buyer_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('product_price', models.CharField(max_length=20)),
                ('product_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=50)),
                ('seller_item', models.CharField(max_length=50)),
                ('seller_cost', models.CharField(max_length=50)),
                ('seller_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.IntegerField()),
                ('order_cost', models.CharField(max_length=20)),
                ('order_date', models.DateField()),
                ('order_name', models.ManyToManyField(to='invsystest.Product')),
            ],
        ),
    ]