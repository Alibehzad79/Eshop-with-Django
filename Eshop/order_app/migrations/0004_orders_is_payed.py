# Generated by Django 3.2.7 on 2021-11-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0003_finalorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='is_payed',
            field=models.BooleanField(default=False),
        ),
    ]
