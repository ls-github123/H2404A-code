# Generated by Django 5.0.6 on 2024-07-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='category',
            field=models.CharField(max_length=10, verbose_name='商品种类'),
        ),
    ]