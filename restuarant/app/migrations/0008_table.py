# Generated by Django 4.1.3 on 2023-06-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_dish_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('booked', models.BooleanField()),
            ],
        ),
    ]