# Generated by Django 3.2.12 on 2022-09-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220506_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('updated_date', models.TimeField(auto_now=True)),
                ('created_date', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
