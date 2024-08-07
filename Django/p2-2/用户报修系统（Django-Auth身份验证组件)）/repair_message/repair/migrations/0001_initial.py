# Generated by Django 5.0.6 on 2024-08-04 11:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upkeep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='报修项目')),
                ('content', models.TextField(verbose_name='项目详情')),
                ('worker', models.CharField(max_length=50, verbose_name='维修人')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='报修时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='报修用户')),
            ],
            options={
                'verbose_name': '报修信息',
                'verbose_name_plural': '报修信息',
                'db_table': 'upkeep',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=5, verbose_name='性别')),
                ('hobby', models.CharField(blank=True, max_length=50, null=True, verbose_name='爱好')),
                ('address', models.CharField(max_length=50, verbose_name='所在城市')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='用户信息简介(备注)')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户基本信息',
                'verbose_name_plural': '用户基本信息',
                'db_table': 'user_profile',
                'managed': True,
            },
        ),
    ]
