# Generated by Django 4.0.5 on 2022-09-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_alter_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='09123456789', max_length=12, verbose_name='شماره تلفن'),
        ),
    ]
