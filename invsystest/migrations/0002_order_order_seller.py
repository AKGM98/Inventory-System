# Generated by Django 2.2.14 on 2021-07-26 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invsystest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='invsystest.Seller'),
        ),
    ]
