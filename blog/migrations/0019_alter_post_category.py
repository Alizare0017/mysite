# Generated by Django 3.2.12 on 2022-11-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20221119_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]