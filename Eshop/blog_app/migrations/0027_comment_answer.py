# Generated by Django 3.2.7 on 2021-10-28 18:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0026_alter_blog_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='answer',
            field=tinymce.models.HTMLField(blank=True, default=None, null=True),
        ),
    ]
