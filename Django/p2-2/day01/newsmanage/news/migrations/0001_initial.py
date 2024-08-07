# Generated by Django 5.0.6 on 2024-07-24 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10, verbose_name='类别')),
            ],
            options={
                'verbose_name': '分类信息',
                'verbose_name_plural': '分类信息',
                'db_table': 'news_category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='新闻标题')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('content', models.TextField(verbose_name='新闻内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_items', to='news.newscategory', verbose_name='新闻类别')),
            ],
            options={
                'verbose_name': '新闻条目',
                'verbose_name_plural': '新闻条目',
                'db_table': 'news_item',
                'managed': True,
            },
        ),
    ]
