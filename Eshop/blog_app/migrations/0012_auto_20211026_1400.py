# Generated by Django 3.2.7 on 2021-10-26 10:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_auto_20211025_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 26, 14, 0, 35, 930492)),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('date_add_to_history', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.blog')),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'Histories',
            },
        ),
    ]
