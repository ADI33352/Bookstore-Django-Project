# Generated by Django 3.0.8 on 2021-04-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210418_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='imagee',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
