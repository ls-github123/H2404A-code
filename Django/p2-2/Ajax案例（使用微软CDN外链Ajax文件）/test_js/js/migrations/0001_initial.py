# Generated by Django 5.0.6 on 2024-08-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
