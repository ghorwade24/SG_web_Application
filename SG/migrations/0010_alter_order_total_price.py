# Generated by Django 4.1.13 on 2024-12-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SG', '0009_alter_orderitem_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
