# Generated by Django 3.2.7 on 2021-11-10 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0004_orders_is_payed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finalorder',
            old_name='is_accept',
            new_name='is_sent',
        ),
    ]
