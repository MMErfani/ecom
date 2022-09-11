# Generated by Django 4.0.5 on 2022-09-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_product_description_alter_product_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='آدرس')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت نمایش')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
    ]
