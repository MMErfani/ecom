# Generated by Django 4.1.1 on 2022-09-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0017_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='purchased_products',
            field=models.ManyToManyField(blank=True, to='frontend.product', verbose_name='محصولات خریداری شده'),
        ),
    ]
