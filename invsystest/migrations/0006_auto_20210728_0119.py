# Generated by Django 2.2.14 on 2021-07-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invsystest', '0005_auto_20210728_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
