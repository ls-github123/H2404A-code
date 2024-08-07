# Generated by Django 5.0.6 on 2024-07-27 10:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=20, verbose_name='书名')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('publish', models.CharField(max_length=30, verbose_name='出版社')),
                ('createtime', models.DateField(verbose_name='出版时间')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='零售价格')),
                ('num', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='库存数量')),
                ('sale', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='销售数量')),
                ('sell', models.BooleanField(default=False, verbose_name='是否上架')),
                ('cover', models.ImageField(default='https://static.djangoproject.com/img/logos/django-logo-negative.png', upload_to='', verbose_name='封面图片路径')),
            ],
            options={
                'verbose_name': '书籍信息',
                'verbose_name_plural': '书籍信息',
                'db_table': 'book_info',
                'managed': True,
            },
        ),
    ]
