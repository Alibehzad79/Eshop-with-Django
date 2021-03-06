# Generated by Django 3.2.7 on 2021-10-11 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0001_initial'),
        ('shop_app', '0008_auto_20211009_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.CreateModel(
            name='CategoryClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('category_mother', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='category_app.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='cateories',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop_app.categoryclass'),
        ),
    ]
