# Generated by Django 3.2.7 on 2021-10-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0012_productreview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name': 'ProductReview', 'verbose_name_plural': 'ProductReviews'},
        ),
        migrations.AddField(
            model_name='productreview',
            name='is_accept',
            field=models.BooleanField(default=False),
        ),
    ]
