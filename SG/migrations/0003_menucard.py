# Generated by Django 5.1 on 2024-10-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SG', '0002_enquriforfranchasi_fooditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(choices=[('Pani Puri', 'Pani Puri'), ('Masala Puri', 'Masala Puri'), ('Ragada Puri', 'Ragada Puri'), ('Dahi Puri', 'Dahi Puri'), ('Shev Puri', 'Shev Puri'), ('SPDP', 'SPDP'), ('Sukhi Bhel', 'Sukhi Bhel'), ('Aoli Bhel', 'Aoli Bhel'), ('Farasan Bhel', 'Farasan Bhel')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
