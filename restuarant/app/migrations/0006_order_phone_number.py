# Generated by Django 4.1.3 on 2023-06-01 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
