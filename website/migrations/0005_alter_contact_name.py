# Generated by Django 3.2.12 on 2022-11-22 07:36

from django.db import migrations, models
import django_extensions.validators


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=64, validators=[django_extensions.validators.HexValidator(length=64)]),
        ),
    ]
